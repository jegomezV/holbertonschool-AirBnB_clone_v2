#!/usr/bin/python3
""""""
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

class DBStorage:
    """"""
    __engine = None
    __session = None

    def __init__(self):
        """"""
        self.__engine = create_engine('mysql+mysqldb://HBNB_MYSQL_USER:HBNB_MYSQL_PWD@HBNB_MYSQL_HOST/HBNB_MYSQL_DB', pool_pre_ping=True)
        metadata = MetaData()

        if os.getenv("HBNB_ENV") == "test":
            metadata.drop_all()

    def all(self, cls=None):
        """"""
        dic = {}
        session_market = sessionmaker(bind=self.__engine)
        with session_market() as session:
            if cls is None:
                    for obj in self.__session.query(cls).all():
                        dic[obj.to_dict()['class'] + '.' + obj.id] = obj
            else:
                 for obj in self.__session.query(cls).all():
                    if obj.id == cls.id:
                        dic[obj.to_dict()['class'] + '.' + obj.id] = obj
            return dic
