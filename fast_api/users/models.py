from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'User'

    user_id = Column(Integer, primary_key=True)
    rut = Column(String(12))
    email = Column(String(255), unique=True)
    password = Column(String(128))
    phone_number = Column(String(20))
    address = Column(String(255))
