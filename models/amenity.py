#!/usr/bin/python3
"""Amenity Module for HBNB project"""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table
from sqlalchemy.orm import relationship


association_table = Table('place_amenity', Base.metadata,
                          Column(
                              'place_id', String(60), primary_key=True,
                              nullable=False),
                          Column(
                              'amenity_id', String(60), primary_key=True,
                              nullable=False))


class Amenity(BaseModel, Base):
    """Amenity class"""

    __tablename__ = 'amenities'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)

        place_amenities = relationship(
                "Place", secondary=association_table,
                backref="amenities")
    else:
        name = ''
