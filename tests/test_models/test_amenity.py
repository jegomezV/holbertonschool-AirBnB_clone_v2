#!/usr/bin/python3
""" Unittest for Amenity class """
""" Unittest for Amenity class """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import pycodestyle
import pycodestyle


class test_Amenity(test_basemodel):
    """ Test cases for Amenity class """
    """ Test cases for Amenity class """

    def __init__(self, *args, **kwargs):
        """ Init method """
        """ Init method """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ Test for name type """
        """ Test for name type """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_docs(self):
        """ Test for doc """
        self.assertIsNotNone(Amenity.__doc__)