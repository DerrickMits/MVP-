#!/usr/bin/python3
""" holds class Facility"""
import hospital_models as models
from hospital_models.base_model import HospitalBaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

if models.storage_t == 'db':
    facility_amenity = Table('facility_amenity', Base.metadata,
                             Column('facility_id', String(60),
                                    ForeignKey('facilities.id', onupdate='CASCADE',
                                               ondelete='CASCADE'),
                                    primary_key=True),
                             Column('amenity_id', String(60),
                                    ForeignKey('amenities.id', onupdate='CASCADE',
                                               ondelete='CASCADE'),
                                    primary_key=True))


class Facility(HospitalBaseModel, Base):
    """Representation of Facility """
    if models.storage_t == 'db':
        __tablename__ = 'facilities'
        department_id = Column(String(60), ForeignKey('departments.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_capacity = Column(Integer, nullable=False, default=0)
        price_per_day = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="facility")
        amenities = relationship("Amenity", secondary="facility_amenity",
                                 backref="facility_amenities",
                                 viewonly=False)
    else:
        department_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_capacity = 0
        price_per_day = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initializes Facility"""
        super().__init__(*args, **kwargs)

    if models.storage_t != 'db':
        @property
        def reviews(self):
            """getter attribute returns the list of Review instances"""
            from hospital_models.review import Review
            review_list = []
            all_reviews = models.storage.all(Review)
            for review in all_reviews.values():
                if review.facility_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """getter attribute returns the list of Amenity instances"""
            from hospital_models.amenity import Amenity
            amenity_list = []
            all_amenities = models.storage.all(Amenity)
            for amenity in all_amenities.values():
                if amenity.facility_id == self.id:
                    amenity_list.append(amenity)
            return amenity_list
