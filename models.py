from sqlalchemy import Column, Integer, String, Table, ForeignKey, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

word_tab_association = Table(
    'word_tab',
    Base.metadata,
    Column('word_id', Integer, ForeignKey('words.id')),
    Column('tab_id', Integer, ForeignKey('tabs.id'))
)


class Word(Base):
    __tablename__ = 'words'

    id = Column(Integer, primary_key=True)
    word = Column(String, unique=True, nullable=False)
    pinyin = Column(String, nullable=False)
    meaning = Column(String, nullable=False)
    tab_ids = relationship('Tab', secondary=word_tab_association, back_populates='words')

    def __init__(self, word, pinyin, meaning):
        self.word = word
        self.pinyin = pinyin
        self.meaning = meaning

    def __to_dict__(self):
        return {
            'id': self.id,
            'word': self.word,
            'meaning': self.meaning,
            'pinyin': self.pinyin
        }


class Tab(Base):
    __tablename__ = 'tabs'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False, nullable=False)
    words = relationship('Word', secondary=word_tab_association, back_populates='tab_ids')

    def __init__(self, name):
        self.name = name

    def __to_dict__(self):
        return {
            'id': self.id,
            'name': self.name
        }


@event.listens_for(Word, 'after_delete')
def remove_word_from_tabs(mapper, connection, target):
    connection.execute(
        word_tab_association.delete().where(
            word_tab_association.c.word_id == target.id
        )
    )


@event.listens_for(Tab, 'after_delete')
def remove_tab_from_words(mapper, connection, target):
    connection.execute(
        word_tab_association.delete().where(
            word_tab_association.c.tab_id == target.id
        )
    )
