#!/usr/bin/python3
""" This is the Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models import storage_type

class Amenity(BaseModel, Base):
    """ This class is used to store amenity information """
    __tablename__ = 'amenities'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
