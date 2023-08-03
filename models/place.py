#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship


place_amenity = Table("place_amenity",
                      Base.metadata,
                      Column(
                          "place_id",
                          String(60),
                          ForeignKey("places.id"),
                          primary_key=True,
                          nullable=False),
                      Column(
                          "amenity_id",
                          String(60),
                          ForeignKey("amenities.id"),
                          primary_key=True,
                          nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
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

    amenity_ids = []

    # DBStorage
    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place", cascade='delete')
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False, overlaps="place_amenities")
    else:
        # FileStorage
        @property
        def reviews(self):
            """"""
            from models import storage
            from models.review import Review
            review_dict = storage.all(Review)
            review_list = []
            for key, value in review_dict.items():
                if value.place_id == self.id:
                    review_list.append(value)
            return review_list

        @property
        def amenities(self):
            """"""
            from models import storage
            from models.amenity import Amenity
            amenity_dict = storage.all(Amenity)
            amenity_list = []
            for key, value in amenity_dict.items():
                if value.id in self.amenity_ids:
                    amenity_list.append(value)
            return amenity_list

        @amenities.setter
        def amenities(self, object=None):
            """"""
            from models.amenity import Amenity
            if object and isinstance(object, Amenity):
                self.amenity_ids.append(object.id)
