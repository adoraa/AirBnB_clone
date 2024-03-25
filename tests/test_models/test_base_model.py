#!/usr/bin/python3
"""Defines unittests for models/base_model.py.
Unittest classes:
    TestBaseModel_Instantiation
    TestBase_Instance_Print
    TestBaseModel_Save
    TestBase_from_json_string
    TestBaseModel_to_dict
"""

import unittest
import json
import re
from models.base_model import BaseModel
from datetime import datetime
from time import sleep

class TestBaseModelInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def setUp(self):
        self.base_model = BaseModel()

    def test_instance(self):
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertEqual(str(type(self.base_model)), "<class 'models.base_model.BaseModel'>")
        self.assertTrue(issubclass(type(self.base_model), BaseModel))

class TestBaseModelInstancePrint(unittest.TestCase):
    """Unittest for testing the __str__ method."""

    def setUp(self):
        self.base_model = BaseModel()

    def test_str_return(self):
        self.assertEqual(str(self.base_model),
                         "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__))

    def test_str(self):
        string = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(string, str(self.base_model))

class TestBaseModelSaveMethod(unittest.TestCase):
    """Unittest for testing the save method."""

    def setUp(self):
        self.base_model = BaseModel()

    def test_save(self):
        updated_at_1 = self.base_model.updated_at
        self.base_model.save()
        updated_at_2 = self.base_model.updated_at
        self.assertNotEqual(updated_at_1, updated_at_2)

    def test_save_updates_timestamp(self):
        first_updated_at = self.base_model.updated_at
        sleep(0.05)
        self.base_model.save()
        self.assertLess(first_updated_at, self.base_model.updated_at)

    def test_multiple_saves(self):
        first_updated_at = self.base_model.updated_at
        sleep(0.05)
        self.base_model.save()
        second_updated_at = self.base_model.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        self.base_model.save()
        self.assertLess(second_updated_at, self.base_model.updated_at)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            self.base_model.save(None)

class TestBaseModelToDictMethod(unittest.TestCase):
    """Unittest for testing the to_dict method of the BaseModel class."""

    def setUp(self):
        self.base_model = BaseModel()

    def test_class_name_present(self):
        dic = self.base_model.to_dict()
        self.assertNotEqual(dic, self.base_model.__dict__)

    def test_attribute_iso_format(self):
        dic = self.base_model.to_dict()
        self.assertEqual(type(dic['created_at']), str)
        self.assertEqual(type(dic['updated_at']), str)


if __name__ == '__main__':
    unittest.main()

