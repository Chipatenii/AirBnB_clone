#!/usr/bin/python3
"""
unittest for models/city.py
Test case:
    Test_state
    Test_name
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def test_state_id_initialization(self):
        city = City()
        self.assertEqual(city.state_id, "")

    def test_name_initialization(self):
        city = City()
        self.assertEqual(city.name, "")

    def test_state_id_assignment(self):
        city = City()
        city.state_id = "CA"
        self.assertEqual(city.state_id, "CA")

    def test_name_assignment(self):
        city = City()
        city.name = "Nairobi"
        self.assertEqual(city.name, "Nairobi")


if __name__ == "__main__":
    unittest.main()
