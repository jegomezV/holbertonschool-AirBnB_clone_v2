#!/usr/bin/python3
""""""
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
    """"""
    __engine = None
    __session = None

    def __init__(self):
        """"""
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

        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

    def all(self, cls=None):
        """"""

        dic = {}
        if cls:
            for obj in self.__session.query(cls).all():
                dic[type(obj).__name__ + '.' + obj.id] = obj
        else:
            for cls in [City, State]:
                for obj in self.__session.query(cls).all():
                    dic[type(obj).__name__ + '.' + obj.id] = obj

        return dic

    def new(self, obj):
        """"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """"""
        self.__session.commit()

    def delete(self, obj=None):
        """"""
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()
