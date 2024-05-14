from database.database import db_session
from models import Tab, Word

db = db_session


def add_words_to_tab(w: Word, t: Tab):
    t.words.append(w)
    db.commit()
