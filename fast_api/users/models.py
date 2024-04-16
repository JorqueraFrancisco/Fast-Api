from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from config.database import Base


class User(Base):
    __tablename__ = 'users'

    user_id = Column(
        Integer,
        primary_key=True
    )
    rut = Column(
        String(12),
        default='11111111-1'
    )
    email = Column(String(255), unique=True)
    password = Column(String(128))
    phone_number = Column(
        String(20),
        default='+56988888888'
    )
    address = Column(
        String(255),
        default='default direction'
    )
    is_active = Column(
        Boolean,
        default=True
    )
    orders = relationship("Order", back_populates="user")
