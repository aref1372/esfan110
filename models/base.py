# models/base.py
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from config import DATABASE_URL


Base = declarative_base()
engine = create_engine(DATABASE_URL, echo=True)

# ساخت session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


