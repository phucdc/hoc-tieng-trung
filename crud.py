from gtts import gTTS

from sqlalchemy.exc import IntegrityError, NoResultFound
from models import Word, Tab
from database import db_session
from config import APP_DIR


def get_tab_by_id(tab_id: int) -> None | Tab:
    tab = db_session.query(Tab).filter_by(id=tab_id).one()
    if not tab:
        return
    return tab


def add_tab(name: str) -> None | Tab:
    try:
        tab = Tab(name=name)
        db_session.add(tab)
        db_session.commit()
        return tab
    except IntegrityError as ie:
        return


def delete_tab_by_id(tab_id: int) -> None | Tab:
    try:
        tab = get_tab_by_id(tab_id)
        if not tab:
            return
        db_session.delete(tab)
        db_session.commit()
        return tab
    except NoResultFound as nrf:
        return


def get_word_by_id(word_id: int) -> None | Word:
    word = db_session.query(Word).filter_by(id=word_id).one()
    if not word:
        return
    return word


def add_word(word: str, meaning: str) -> None | Word:
    try:
        voice_path = f'{word}.mp3'
        w = Word(word=word, meaning=meaning, voice_path=voice_path)
        db_session.add(w)
        db_session.commit()
        tts = gTTS(text=word, lang='zh-cn')
        tts.save(f'{APP_DIR}/voices/{voice_path}')
    except IntegrityError as ie:
        return


def delete_word_by_id():
    ...
