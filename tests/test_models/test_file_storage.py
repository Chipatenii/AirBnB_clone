#!/usr/bin/python3
"""
Defines unittests for models/engine/file_storage.py.

Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import unittest
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """class representing test for file storage engine"""

    def setUp(self):
        self.file_path = "file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path
        self.base_model = BaseModel()
        self.user = User()
        self.state = State()
        self.city = City()
        self.amenity = Amenity()
        self.place = Place()
        self.review = Review()
        self.storage.new(self.base_model)
        self.storage.new(self.user)
        self.storage.new(self.state)
        self.storage.new(self.city)
        self.storage.new(self.amenity)
        self.storage.new(self.place)
        self.storage.new(self.review)
        self.storage.save()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        expected_length = len(all_objects)
        self.assertEqual(len(all_objects), expected_length)

    def test_new(self):
        new_model = BaseModel()
        self.storage.new(new_model)
        self.assertIn("BaseModel.{}".format(new_model.id), self.storage.all())

    def test_save(self):
        self.storage.save()
        with open(self.file_path, 'r') as f:
            data = json.load(f)
            self.assertIn("BaseModel.{}".format(self.base_model.id), data)
            self.assertIn("User.{}".format(self.user.id), data)
            self.assertIn("State.{}".format(self.state.id), data)
            self.assertIn("City.{}".format(self.city.id), data)
            self.assertIn("Amenity.{}".format(self.amenity.id), data)
            self.assertIn("Place.{}".format(self.place.id), data)
            self.assertIn("Review.{}".format(self.review.id), data)

    def test_reload(self):
        new_model = BaseModel()
        new_model_key = "BaseModel.{}".format(new_model.id)
        self.storage.new(new_model)
        self.storage.save()
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertIn(new_model_key, all_objects)
        self.assertIsInstance(all_objects[new_model_key], BaseModel)
        self.assertNotIsInstance(all_objects[new_model_key], User)
        self.assertNotIsInstance(all_objects[new_model_key], State)
        self.assertNotIsInstance(all_objects[new_model_key], City)
        self.assertNotIsInstance(all_objects[new_model_key], Amenity)
        self.assertNotIsInstance(all_objects[new_model_key], Place)
        self.assertNotIsInstance(all_objects[new_model_key], Review)


if __name__ == '__main__':
    unittest.main()
