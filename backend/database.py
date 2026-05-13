from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# database
DATABASE = 'todo.py'

SQL_DATABASE_URL = f"sqlite:///{DATABASE}"

engine = create_engine(
    SQL_DATABASE_URL,
    connect_args={"check_same_thread":False}
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autoCommit=False
)

Base = declarative_base()