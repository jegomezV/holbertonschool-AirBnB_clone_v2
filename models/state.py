#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    # FileStorage
    if getenv("HBNB_TYPE_STORANGE") in (None, "fs"):
        @property
        def cities(self):
            """return the cities by state"""
            from models import storage
            from models.city import City
            cities_dict = storage.all(City)
            city_list = []
            for key, value in cities_dict.items():
                if value.state_id == self.id:
                    city_list.append(value)
            return city_list

    # DBStorage
    if getenv("HBNB_TYPE_STORANGE") == "db":
        cities = relationship('City', backref='state', cascade='all, delete')
