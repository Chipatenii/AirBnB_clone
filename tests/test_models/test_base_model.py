#!/usr/bin/python3
"""
Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_setUp
    TestBaseModel_test_init
    TestBaseModel_test_str
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_init(self):
        # Test if id is a string
        self.assertIsInstance(self.base_model.id, str)

        # Test if created_at and updated_at are datetime objects
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str(self):
        # Test string representation of the <link>BaseModel</link> instance
        expected_str = "[BaseModel] ({}) {}".format(
                self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_save(self):
        # Test save method
        previous_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(previous_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        # Test to_dict method
        dict_obj = self.base_model.to_dict()
        self.assertIsInstance(dict_obj, dict)
        self.assertEqual(dict_obj["__class__"], "BaseModel")
        self.assertEqual(dict_obj["id"], self.base_model.id)
        self.assertEqual(
                dict_obj["created_at"],
                self.base_model.created_at.isoformat())
        self.assertEqual(
                dict_obj["updated_at"],
                self.base_model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
