#!/usr/bin/python3
"""
Contains the class HospitalDBStorage
"""

import hospital_models as models
from hospital_models.amenity import Amenity
from hospital_models.base_model import HospitalBaseModel, Base
from hospital_models.unit import Unit
from hospital_models.facility import Facility
from hospital_models.review import Review
from hospital_models.department import Department
from hospital_models.user import HospitalUser
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Amenity": Amenity, "Unit": Unit,
           "Facility": Facility, "Review": Review, "Department": Department, "HospitalUser": HospitalUser}


class HospitalDBStorage:
    """interacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a HospitalDBStorage object"""
        HOSPITAL_MYSQL_USER = getenv('HOSPITAL_MYSQL_USER')
        HOSPITAL_MYSQL_PWD = getenv('HOSPITAL_MYSQL_PWD')
        HOSPITAL_MYSQL_HOST = getenv('HOSPITAL_MYSQL_HOST')
        HOSPITAL_MYSQL_DB = getenv('HOSPITAL_MYSQL_DB')
        HOSPITAL_ENV = getenv('HOSPITAL_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HOSPITAL_MYSQL_USER,
                                             HOSPITAL_MYSQL_PWD,
                                             HOSPITAL_MYSQL_HOST,
                                             HOSPITAL_MYSQL_DB))
        if HOSPITAL_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
