#!/usr/bin/python3
"""
Test for models/state.py
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_name_initialization(self):
        state = State()
        self.assertEqual(state.name, "")


if __name__ == "__main__":
    unittest.main()
