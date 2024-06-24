#!/usr/bin/python3
""" holds class Unit"""
import hospital_models as models
from hospital_models.base_model import HospitalBaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Unit(HospitalBaseModel, Base):
    """Representation of a hospital unit """
    if models.storage_t == "db":
        __tablename__ = 'units'
        department_id = Column(String(60), ForeignKey('departments.id'), nullable=False)
        name = Column(String(128), nullable=False)
        facilities = relationship("Facility", backref="unit")
    else:
        department_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes unit"""
        super().__init__(*args, **kwargs)
