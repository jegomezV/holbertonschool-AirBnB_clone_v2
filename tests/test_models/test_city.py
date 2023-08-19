#!/usr/bin/python3
""" Unittest for City class """
""" Unittest for City class """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import pycodestyle
import pycodestyle


class test_City(test_basemodel):
    """ Test cases for City class """
    """ Test cases for City class """

    def __init__(self, *args, **kwargs):
        """ Init method """
        """ Init method """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ Test for stated_id type """
        """ Test for stated_id type """
        new = self.value()
        self.assertNotEqual(type(new.state_id), str)
        self.assertNotEqual(type(new.state_id), str)

    def test_name(self):
        """ Test for name type """
        """ Test for name type """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_docs(self):
        """ Test for doc """
        self.assertIsNotNone(City.__doc__)