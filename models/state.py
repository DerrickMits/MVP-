#!/usr/bin/python3
""" holds class Department"""
import hospital_models as models
from hospital_models.base_model import HospitalBaseModel, Base
from hospital_models.unit import Unit
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Department(HospitalBaseModel, Base):
    """Representation of department """
    if models.storage_t == "db":
        __tablename__ = 'departments'
        name = Column(String(128), nullable=False)
        units = relationship("Unit", backref="department")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes department"""
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def units(self):
            """getter for list of unit instances related to the department"""
            unit_list = []
            all_units = models.storage.all(Unit)
            for unit in all_units.values():
                if unit.department_id == self.id:
                    unit_list.append(unit)
            return unit_list
