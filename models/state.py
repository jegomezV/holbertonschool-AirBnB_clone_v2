#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="state", cascade="all, delete-orphan")

    @property
    def cities(self):
        """return the cities by state"""
        from models import storage
        from models.city import City
        cities_dict = storage.all(City)
        city_list:list
        for key, value in cities_dict.items():
            if value.state_id == self.id:
                city_list.append(value)
        return city_list
