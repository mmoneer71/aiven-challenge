from consumer.settings import (
    PSQL_HOST,
    PSQL_NAME,
    PSQL_PASSWORD,
    PSQL_PORT,
    PSQL_USERNAME,
)
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

DATABASE_URL = f"postgresql://{PSQL_USERNAME}:{PSQL_PASSWORD}@{PSQL_HOST}:{PSQL_PORT}/{PSQL_NAME}?sslmode=require"

engine = create_engine(DATABASE_URL)
conn = engine.connect()
session = sessionmaker()
session.configure(bind=engine)
db_session = session()
Base = declarative_base()


def get_db_session() -> Session:
    global db_session
    try:
        db_session.commit()
    except SQLAlchemyError:
        db_session = session()
    return db_session
