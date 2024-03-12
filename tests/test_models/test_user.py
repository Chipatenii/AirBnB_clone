#!/usr/bin/python3
"""
Defines unittests for models/user.py.
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def test_email_initialization(self):
        user = User()
        self.assertEqual(user.email, "")

    def test_password_initialization(self):
        user = User()
        self.assertEqual(user.password, "")

    def test_first_name_initialization(self):
        user = User()
        self.assertEqual(user.first_name, "")

    def test_last_name_initialization(self):
        user = User()
        self.assertEqual(user.last_name, "")


if __name__ == "__main__":
    unittest.main()
