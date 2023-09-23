#!/usr/bin/python3
"""This module will define a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """This class will define a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship('Place', backref='user', cascade='all, delete, delete-orphan')
    reviews = relationship('Review', backref='user', cascade='all, delete, delete-orphan')
