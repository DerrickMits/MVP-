#!/usr/bin/python3
""" holds class HospitalUser"""
import hospital_models as models
from hospital_models.base_model import HospitalBaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class HospitalUser(HospitalBaseModel, Base):
    """Representation of a hospital user """
    if models.storage_t == 'db':
        __tablename__ = 'hospital_users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        # Assuming relationships for other entities in the hospital management system
        appointments = relationship("Appointment", backref="hospital_user")
        records = relationship("MedicalRecord", backref="hospital_user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes hospital user"""
        super().__init__(*args, **kwargs)
