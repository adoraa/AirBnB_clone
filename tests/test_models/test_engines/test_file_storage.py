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

    def test_file_path_existence(self):
        """Test that the file path defined in __file_path exists."""
        directory = os.path.dirname(self.storage._FileStorage__file_path)
        self.assertTrue(os.path.exists(directory))

    def test_reload_empty_file(self):
        """Test reload() method with empty JSON file."""
        with open("file.json", "w") as f:
            f.write("")
        self.storage.reload()
       self.assertEqual(len(self.storage._FileStorage__objects), 0)

    def test_class_deserialization(self):
        """Test that objects loaded from JSON file are instances of correct classes."""
        base_model_instance = BaseModel()
        user_instance = User()
        self.storage.new(base_model_instance)
        self.storage.new(user_instance)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        reloaded_objects = self.storage.all()
        self.assertIsInstance(reloaded_objects[f"BaseModel.{base_model_instance.id}"], BaseModel)
        self.assertIsInstance(reloaded_objects[f"User.{user_instance.id}"], User)

    def test_object_attributes(self):
        """Test that attributes of reloaded objects match attributes of original objects."""
        base_model_instance = BaseModel()
        base_model_instance.name = "Test"
        base_model_instance.number = 123
        user_instance = User()
        user_instance.email = "test@example.com"
        user_instance.password = "password"

        self.storage.new(base_model_instance)
        self.storage.new(user_instance)
        self.storage.save()

        self.storage._FileStorage__objects = {}

        self.storage.reload()

        reloaded_objects = self.storage.all()
        reloaded_base_model = reloaded_objects[f"BaseModel.{base_model_instance.id}"]
        reloaded_user = reloaded_objects[f"User.{user_instance.id}"]

        self.assertEqual(base_model_instance.name, reloaded_base_model.name)
        self.assertEqual(base_model_instance.number, reloaded_base_model.number)
        self.assertEqual(user_instance.email, reloaded_user.email)
        self.assertEqual(user_instance.password, reloaded_user.password)

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

    def test_reload_file_not_found(self):
        """Test reload() method handles FileNotFoundError."""
        with patch("builtins.open") as mock_open:
            mock_open.side_effect = FileNotFoundError
            self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)

    def test_delete(self):
        """Test deletion of objects from __objects dictionary and JSON file."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.storage.delete(obj)
        self.assertNotIn(obj_key, self.storage.all())
        with open("file.json", "r") as f:
            file_data = f.read()
            self.assertNotIn(obj_key, file_data)

    def test_invalid_json(self):
        """Test behavior when JSON file contains invalid data."""
        valid_obj = BaseModel()
        self.storage.new(valid_obj)
        self.storage.save()
        with open("file.json", "w") as f:
            f.write("Invalid JSON data")
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)

    def test_save_and_reload_multiple_objects(self):
        """Test save() and reload() methods with multiple objects."""
        obj1 = BaseModel()
        obj2 = User(email="test@example.com", password="123456",
                    first_name="John", last_name="Doe")
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()
        self.storage.reload()
        self.assertIn("BaseModel." + obj1.id, self.storage.all())
        self.assertIn("User." + obj2.id, self.storage.all())


if __name__ == "__main__":
    unittest.main()
