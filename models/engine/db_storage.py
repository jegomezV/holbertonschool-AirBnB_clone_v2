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

    def all(self, cls=None):
        """"""

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
        Session_tmp = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session_tmp)
        self.__session = Session()

# echo 'create Place city_id="11f97478-4bb9-40bb-a4b9-54747837d141" user_id="4fc49084-dcf1-4281-a7f8-8cb911e350e5" name="Lovely_place" number_rooms=3 number_bathrooms=1 max_guest=6 price_by_night=120 latitude=37.773972 longitude=-122.431297' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py