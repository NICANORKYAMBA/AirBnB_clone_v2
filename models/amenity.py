#!/usr/bin/python3
"""Amenity Module for HBNB project"""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship


place_amenity= Table('place_amenity', Base.metadata,
                          Column(
                              'place_id', String(60), ForeignKey('places.id'),
                              nullable=False),
                          Column(
                              'amenity_id', String(60), ForeignKey('amenities.id'),
                              nullable=False))


class Amenity(BaseModel, Base):
    """Amenity class"""

    __tablename__ = 'amenities'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)

        place_amenities = relationship(
                "Place", secondary=place_amenity,
                backref="amenities")
    else:
        name = ''
