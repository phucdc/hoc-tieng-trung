from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

word_tab_association = Table(
    'word_tab_association',
    Base.metadata,
    Column('word_id', Integer, ForeignKey('words.id'), primary_key=True),
    Column('tab_id', Integer, ForeignKey('tabs.id'), primary_key=True)
)


class Word(Base):
    __tablename__ = 'words'
    id = Column(Integer, primary_key=True)
    word = Column(String, unique=True)
    meaning = Column(String, nullable=False)
    voice_path = Column(String, nullable=False, unique=True)

    tabs = relationship(
        'Tab',
        secondary=word_tab_association,
        back_populates='words',
        single_parent=True,
        cascade='delete, delete-orphan'
    )


class Tab(Base):
    __tablename__ = 'tabs'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False, unique=True)

    words = relationship(
        'Word',
        secondary=word_tab_association,
        back_populates='tabs'
    )
