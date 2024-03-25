#!/usr/bin/python3
"""Unittest for file_storage module."""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class."""

    def setUp(self):
        """Set up test environment."""
        self.storage = FileStorage()

    def tearDown(self):
        """Tear down test environment."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_attributes(self):
        """Test attributes of FileStorage instance."""
        self.assertTrue(hasattr(self.storage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(self.storage, "_FileStorage__objects"))

    def test_all(self):
        """Test all() method."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test new() method."""
        obj = BaseModel()
        self.storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test save() method."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        with open("file.json", "r") as f:
            self.assertIn(key, f.read())

    def test_reload(self):
        """Test reload() method."""
        obj = BaseModel()
        obj.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.all())


if __name__ == "__main__":
    unittest.main()
