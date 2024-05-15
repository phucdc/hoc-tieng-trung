from sqlalchemy.exc import IntegrityError

from database.database import db_session
from models import Tab

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
