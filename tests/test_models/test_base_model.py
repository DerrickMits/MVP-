#!/usr/bin/python3
""" Module of Unittests """
import unittest
from models.patient import Patient
import datetime


class PatientTests(unittest.TestCase):
    """ Suite of Tests for Patient Class """

    my_patient = Patient()

    def testPatientAttributes(self):
        """ Test attributes value of a Patient instance """

        self.my_patient.name = "John Doe"
        self.my_patient.patient_id = "12345"
        self.my_patient.admission_date = datetime.datetime(2023, 6, 1, 12, 0, 0)
        self.my_patient.discharge_date = datetime.datetime(2023, 6, 10, 12, 0, 0)
        self.my_patient.save()
        patient_json = self.my_patient.to_dict()

        self.assertEqual(self.my_patient.name, patient_json['name'])
        self.assertEqual(self.my_patient.patient_id, patient_json['patient_id'])
        self.assertEqual('Patient', patient_json['__class__'])
        self.assertEqual(self.my_patient.id, patient_json['id'])
        self.assertEqual(self.my_patient.admission_date.isoformat(), patient_json['admission_date'])
        self.assertEqual(self.my_patient.discharge_date.isoformat(), patient_json['discharge_date'])

    def testSave(self):
        """ Checks if save method updates the public instance
        attribute updated_at """
        self.my_patient.name = "Jane Doe"
        self.my_patient.save()

        self.assertIsInstance(self.my_patient.id, str)
        self.assertIsInstance(self.my_patient.created_at, datetime.datetime)
        self.assertIsInstance(self.my_patient.updated_at, datetime.datetime)

        first_dict = self.my_patient.to_dict()

        self.my_patient.name = "John Smith"
        self.my_patient.save()
        sec_dict = self.my_patient.to_dict()

        self.assertEqual(first_dict['created_at'], sec_dict['created_at'])
        self.assertNotEqual(first_dict['updated_at'], sec_dict['updated_at'])

if __name__ == '__main__':
    unittest.main()

