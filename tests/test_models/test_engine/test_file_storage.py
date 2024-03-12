import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_path = "file.json"
        self.file_storage = FileStorage()

    def tearDown(self):
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    """def test_all(self):
        self.file_storage._FileStorage__objects ={}

        actual_result = self.file_storage.all()
        expected_result = self.file_storage._FileStorage__objects
        self.assertEqual(
                actual_result, expected_result,
                f"Expected: {expected_result}, Got: {actual_result}"
                )"""

    def test_new(self):
        base_model = BaseModel()
        self.file_storage.new(base_model)
        key = "{}.{}".format(base_model.__class__.__name__, base_model.id)
        self.assertIn(key, self.file_storage.all())

    def test_save(self):
        base_model = BaseModel()
        self.file_storage.new(base_model)
        self.file_storage.save()
        self.assertTrue(os.path.isfile(self.file_path))

    def test_classes(self):
        classes = self.file_storage.classes()
        self.assertIsInstance(classes, dict)
        self.assertIn("BaseModel", classes)
        self.assertIn("User", classes)
        self.assertIn("State", classes)
        self.assertIn("City", classes)
        self.assertIn("Amenity", classes)
        self.assertIn("Place", classes)
        self.assertIn("Review", classes)

    def test_attributes(self):
        attributes = self.file_storage.attributes()
        self.assertIsInstance(attributes, dict)
        for attr in attributes.values():
            self.assertIsInstance(attr, dict)
            for value in attr.values():
                self.assertTrue(value in [str, int, float, list, datetime])

    def test_reload(self):
        base_model = BaseModel()
        self.file_storage.new(base_model)
        self.file_storage.save()
        self.file_storage = FileStorage()
        self.file_storage.reload()
        key = "{}.{}".format(base_model.__class__.__name__, base_model.id)
        self.assertIn(key, self.file_storage.all())


if __name__ == '__main__':
    unittest.main()
