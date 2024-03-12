#!/usr/bin/python3
"""
Test for models/place.py
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_city_id_initialization(self):
        place = Place()
        self.assertEqual(place.city_id, "")

    def test_user_id_initialization(self):
        place = Place()
        self.assertEqual(place.user_id, "")

    def test_name_initialization(self):
        place = Place()
        self.assertEqual(place.name, "")

    def test_description_initialization(self):
        place = Place()
        self.assertEqual(place.description, "")

    def test_number_rooms_initialization(self):
        place = Place()
        self.assertEqual(place.number_rooms, 0)

    def test_number_bathrooms_initialization(self):
        place = Place()
        self.assertEqual(place.number_bathrooms, 0)

    def test_max_guest_initialization(self):
        place = Place()
        self.assertEqual(place.max_guest, 0)

    def test_price_by_night_initialization(self):
        place = Place()
        self.assertEqual(place.price_by_night, 0)

    def test_latitude_initialization(self):
        place = Place()
        self.assertEqual(place.latitude, 0.0)

    def test_longitude_initialization(self):
        place = Place()
        self.assertEqual(place.longitude, 0.0)

    def test_amenity_ids_initialization(self):
        place = Place()
        self.assertEqual(place.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
