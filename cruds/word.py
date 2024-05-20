import random

from gtts import gTTS
from sqlalchemy.exc import IntegrityError, PendingRollbackError

from config import SAVE_VOICE_DIR
from database.database import db_session
from models import Word

db = db_session


def read(word_id: int) -> None | Word:
    word = db.query(Word).filter_by(id=word_id).one()
    if not word:
        return
    return word


def create(word: str, pinyin: str, meaning: str) -> None | Word:
    w = Word(word=word, pinyin=pinyin, meaning=meaning)
    try:
        db.add(w)
        db.commit()
        tts = gTTS(text=word, lang='zh-cn')
        tts.save(f'{SAVE_VOICE_DIR}/{w.word}.mp3')
        return w
    except Exception as e:
        db.rollback()
        return e.__str__


def update(word_id: int, pinyin: str, word: str = None, meaning: str = None) -> None | Word:
    w = db.query(Word).filter_by(Word.id == word_id).one()
    if not w:
        return
    try:
        w.word = word if word else w.word
        w.meaning = meaning if meaning else w.meaning
        w.pinyin = pinyin if pinyin else w.pinyin
        db.commit()
        return w
    except IntegrityError as ie:
        return


def delete(word_id: int) -> None | Word:
    word = read(word_id=word_id)
    if not word:
        return
    try:
        db.delete(word)
        db.commit()
        return word
    except Exception as e:
        return


def get_random_words(page: int=10) -> list:
    all_words = db.query(Word).all()
    if page >= len(all_words):
        return all_words
    return random.sample(all_words, page)


def get_all_words() -> list:
    all_words = db.query(Word).all()
    return all_words
