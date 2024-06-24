#!/usr/bin/python3
"""
Contains the HospitalFileStorage class
"""

import json
from hospital_models.amenity import Amenity
from hospital_models.base_model import HospitalBaseModel as BaseModel
from hospital_models.city import City
from hospital_models.place import Place
from hospital_models.review import Review
from hospital_models.state import State
from hospital_models.user import HospitalUser as User
from hospital_models.facility import Facility
from hospital_models.department import Department

classes = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User,
    "Facility": Facility,
    "Department": Department
}


class HospitalFileStorage:
    """Serializes instances to a JSON file & deserializes back to instances"""

    # Path to the JSON file
    __file_path = "hospital.json"

    # Dictionary to store all objects by <class name>.id
    __objects = {}

    def all(self, cls=None):
        """Returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except FileNotFoundError:
            pass  # No file to reload, initial state remains empty
        except Exception as e:
            print(f"Error reloading JSON file: {e}")

    def delete(self, obj=None):
        """Deletes obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Calls reload() method for deserializing the JSON file to objects"""
        self.reload()
