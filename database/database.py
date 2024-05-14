from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from config import APP_DIR

engine = create_engine(f'sqlite:///{APP_DIR}/database/data.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    from models import Base  # Import Base from models.py
    Base.metadata.create_all(bind=engine)
