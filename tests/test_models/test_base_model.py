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
import os
import re
from datetime import datetime
from time import sleep
from models import storage
from models.base_model import BaseModel


class TestBaseModel_Instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_IsInstanceOf(self):
        """Test instance"""
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)
        self.assertEqual(str(type(b1)), "<class 'models.base_model.BaseModel'>")
        self.assertTrue(issubclass(type(b1), BaseModel))


class TestBaseModel_Instance_Print(unittest.TestCase):
    """Unittest for testing the __str__ method."""

    def test_str_return(self):
        """Unittest for testing the return value of __str__ method."""
        b1 = BaseModel()
        Dika = "[{}] ({}) {}".format("BaseModel", b1.id, str(b1.__dict__))
        self.assertEqual(str(b1), Dika)

    def test_str(self):
        """test that the str method has the correct output"""
        b1 = BaseModel()
        string = "[BaseModel] ({}) {}".format(b1.id, b1.__dict__)
        self.assertEqual(string, str(b1))

    def test_of_str(self):
        """Tests for __str__ method."""
        b1 = BaseModel()
        rex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        res = rex.match(str(b1))
        self.assertIsNotNone(res)
        self.assertEqual(res.group(1), "BaseModel")
        self.assertEqual(res.group(2), b1.id)
        s = res.group(3)
        s = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", s)
        d = json.loads(s.replace("'", '"'))
        d2 = b1.__dict__.copy()
        d2["created_at"] = repr(d2["created_at"])
        d2["updated_at"] = repr(d2["updated_at"])
        self.assertEqual(d, d2)


class TestBaseModel_Save_Method(unittest.TestCase):
    """Unittest for testing the save method."""

    def test_validates_save(self):
        """Check save models"""
        b1 = BaseModel()
        updated_at_1 = b1.updated_at
        b1.save()
        updated_at_2 = b1.updated_at
        self.assertNotEqual(updated_at_1, updated_at_2)

    def test_one_save(self):
        b1 = BaseModel()
        sleep(0.05)
        first_updated_at = b1.updated_at
        b1.save()
        self.assertLess(first_updated_at, b1.updated_at)

    def test_two_saves(self):
        b1 = BaseModel()
        sleep(0.05)
        first_updated_at = b1.updated_at
        b1.save()
        second_updated_at = b1.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        b1.save()
        self.assertLess(second_updated_at, b1.updated_at)

    def test_save_with_arg(self):
        b1 = BaseModel()
        with self.assertRaises(TypeError):
            b1.save(None)


class TestBaseModel_to_Dict_Method(unittest.TestCase):
    """Unittest for testing the to_dict method of the BaseModel class."""

    def test_className_present(self):
        """Test className present"""
        b1 = BaseModel()
        dic = b1.to_dict()
        self.assertNotEqual(dic, b1.__dict__)

    def test_attribute_ISO_format(self):
        """Test datetime field isoformated"""
        b1 = BaseModel()
        dic = b1.to_dict()
        self.assertEqual(type(dic['created_at']), str)
        self.assertEqual(type(dic['updated_at']), str)



if __name__ == '__main__':
    unittest.main()
