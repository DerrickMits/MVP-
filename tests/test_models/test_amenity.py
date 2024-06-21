#!/usr/bin/python3
"""
Unittest for patient.py
"""
import unittest
from models.patient import Patient
import datetime


class TestPatient(unittest.TestCase):
    """Tests instances and methods from Patient class"""

    p = Patient()

    def test_class_exists(self):
        """tests if class exists"""
        res = "<class 'models.patient.Patient'>"
        self.assertEqual(str(type(self.p)), res)

    def test_patient_inheritance(self):
        """test if Patient is a subclass of BaseModel"""
        self.assertIsInstance(self.p, Patient)

    def test_has_attributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.p, 'name'))
        self.assertTrue(hasattr(self.p, 'patient_id'))
        self.assertTrue(hasattr(self.p, 'admission_date'))
        self.assertTrue(hasattr(self.p, 'discharge_date'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.p.name, str)
        self.assertIsInstance(self.p.patient_id, str)
        self.assertIsInstance(self.p.admission_date, datetime.datetime)
        self.assertIsInstance(self.p.discharge_date, datetime.datetime)

if __name__ == '__main__':
    unittest.main()

