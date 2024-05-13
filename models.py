from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Word(Base):
    __tablename__ = 'words'
    id = Column(Integer, primary_key=True)
    word = Column(String, unique=True)
    meaning = Column(String, nullable=False)
    tab_id = Column(Integer, ForeignKey('tabs.id'), nullable=False)


class Tab(Base):
    __tablename__ = 'tabs'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    words = relationship('Word', backref='tab', lazy='dynamic')
