#!/usr/bin/python3
"""
Defining a file storage class
"""
import json
import os
import datetime


class FileStorage:
    """Represents an abstracted storage engine.
    Attributes:
        __file_path (str): filename to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """

        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            serialized_objects = {}
            for key, obj in FileStorage.__objects.items():
                serialized_objects[key] = obj.to_dict()
            json.dump(serialized_objects, file)

    def classes(self):
        """Returns a dictionary of classes"""

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        return {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
                }

    def attributes(self):
        """Returns the valid attributes and their types"""

        return {"BaseModel":
                {"id": str,
                    "created_at": datetime.datetime,
                    "updated_at": datetime.datetime},
                "User":
                {"email": str,
                    "password": str,
                    "first_name": str,
                    "last_name": str},
                "State":
                {"name": str},
                "City":
                {"state_id": str,
                    "name": str},
                "Amenity":
                {"name": str},
                "Place":
                {"city_id": str,
                    "user_id": str,
                    "name": str,
                    "description": str,
                    "number_rooms": int,
                    "number_bathrooms": int,
                    "max_guest": int,
                    "price_by_night": int,
                    "latitude": float,
                    "longitude": float,
                    "amenity_ids": list},
                "Review":
                {"place_id": str,
                    "user_id": str,
                    "text": str}
                }

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            classes = self.classes()
            obj_dict = {key: classes[value["__class__"]](**value)
                        for key, value in obj_dict.items()}
            FileStorage.__objects = obj_dict
