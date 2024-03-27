#!/usr/bin/python3
"""Defines unittests for models/city.py.
Unittest classes:
    TestCity_instantiation
    TestCity_save
    TestCity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City
from models import storage
from models.base_model import BaseModel


class TestCity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_name_is_public_class_attribute(self):
        ct = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(ct))
        self.assertNotIn("name", ct.__dict__)

    def test_state_id_is_public_class_attribute(self):
        ct = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(ct))
        self.assertNotIn("state_id", ct.__dict__)

    def test_two_cities_unique_ids(self):
        ct1 = City()
        ct2 = City()
        self.assertNotEqual(ct1.id, ct2.id)

    def test_two_cities_different_created_at(self):
        ct1 = City()
        sleep(0.05)
        ct2 = City()
        self.assertLess(ct1.created_at, ct2.created_at)

    def test_two_cities_different_updated_at(self):
        ct1 = City()
        sleep(0.05)
        ct2 = City()
        self.assertLess(ct1.updated_at, ct2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        ct = City()
        ct.id = "123456"
        ct.created_at = ct.updated_at = dt
        ctstr = ct.__str__()
        self.assertIn("[City] (123456)", ctstr)
        self.assertIn("'id': '123456'", ctstr)
        self.assertIn("'created_at': " + dt_repr, ctstr)
        self.assertIn("'updated_at': " + dt_repr, ctstr)

    def test_args_unused(self):
        ct = City(None)
        self.assertNotIn(None, ct.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        ct = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(ct.id, "345")
        self.assertEqual(ct.created_at, dt)
        self.assertEqual(ct.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def test_8_instantiation(self):
        """Tests instantiation of City class."""

        b = City()
        self.assertEqual(str(type(b)), "<class 'models.city.City'>")
        self.assertIsInstance(b, City)
        self.assertTrue(issubclass(type(b), BaseModel))


if __name__ == "__main__":
    unittest.main()
