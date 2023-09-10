#!/usr/bin/python3
""" DBStorange for the HNBN project """
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """ That storange in the database """
    __engine = None
    __session = None

    def __init__(self):
        """ Method init for the DBStorange """
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user,
            password,
            host,
            db),
            pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ That returns a list with all instances """

        dic = {}
        if cls:
            for obj in self.__session.query(cls).all():
                dic[type(obj).__name__ + '.' + obj.id] = obj
        else:
            for cls in [City, State, User, Place, Amenity, Review]:
                for obj in self.__session.query(cls).all():
                    dic[type(obj).__name__ + '.' + obj.id] = obj

        return dic

    def new(self, obj):
        """ The add object in self session """
        if obj:
            self.__session.add(obj)

    def save(self):
        """ That save the session """
        self.__session.commit()

    def delete(self, obj=None):
        """"""
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """ That reload the session """
        Base.metadata.create_all(self.__engine)
        Session_tmp = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session_tmp)
        self.__session = Session()

    def close(self):
        """Close the session"""
        self.__session.close()
