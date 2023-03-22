#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from os import getenv
from models.review import Review
from models.amenity import Amenity, place_amenity
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        reviews = relationship("Review", backref="place", cascade="delete")
        amenities = relationship(
                "Amenity", secondary=place_amenity,
                back_populates='place_amenities', viewonly=False)
        amenity_ids = []
    else:
        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """
            Get a list of all linked Reviews.
            """
            review_list = []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        # Define getter and setter for amenities attribute in file storage
        @property
        def amenities(self):
            """
            Getter for amenities attribute that returns a list of Amenity
            instances based on the attribute amenity_ids that contains all
            Amenity.id linked to the Place
            """
            amenity_list = []
            for amenity_id in self.amenity_ids:
                key = "Amenity." + amenity_id
                amenity = models.storage.all(Amenity).get(key)
                if amenity:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            """
            Setter for amenities attribute that handles append method for
            adding an Amenity.id to the attribute amenity_ids. This method
            should accept only Amenity object, otherwise, do nothing.
            """
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
