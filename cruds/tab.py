from sqlalchemy.exc import IntegrityError

from database.database import db_session
from models import Tab
from .word import read as w_read

db = db_session


def read(tab_id: int) -> None | Tab:
    tab = db.query(Tab).filter_by(id=tab_id).one()
    if not tab:
        return
    return tab


def create(name: str) -> None | Tab:
    tab = Tab(name=name)
    try:
        db.add(tab)
        db.commit()
        return tab
    except IntegrityError:
        return


def update(tab_id: int, name: str) -> None | Tab:
    tab = read(tab_id=tab_id)
    if not tab:
        return
    try:
        tab.name = name if name else tab.name
        db.commit()
        return tab
    except IntegrityError as ie:
        return


def delete(tab_id: int) -> None | Tab:
    tab = read(tab_id=tab_id)
    if not tab:
        return
    try:
        db.delete(tab)
        db.commit()
        return tab
    except Exception as e:
        return
    
    
def get_all_tabs() -> list:
    tabs = db.query(Tab).all()
    return tabs


def add_word_to_tab(word_id: int, tab_id: int) -> Tab:
    tab = read(tab_id=tab_id)
    w = w_read(word_id=word_id);
    tab.words.append(w)
    db.commit()
    return tab


def get_words_from_tab(tab_id: int) -> list:
    tab = read(tab_id=tab_id)
    return tab.words
