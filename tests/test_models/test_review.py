#!/usr/bin/python3
""" Unittest for Review class """
""" Unittest for Review class """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import pycodestyle
import pycodestyle


class test_review(test_basemodel):
    """ Test cases for Review class """
    """ Test cases for Review class """

    def __init__(self, *args, **kwargs):
        """ Init method """
        """ Init method """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ Test for place_id type """
        """ Test for place_id type """
        new = self.value()
        self.assertNotEqual(type(new.place_id), str)
        self.assertNotEqual(type(new.place_id), str)

    def test_user_id(self):
        """ Test for user_id type """
        """ Test for user_id type """
        new = self.value()
        self.assertNotEqual(type(new.user_id), str)
        self.assertNotEqual(type(new.user_id), str)

    def test_text(self):
        """ Test for text type """
        """ Test for text type """
        new = self.value()
        self.assertEqual(type(new.text), str)

    def test_docs(self):
        """ Test for doc """
        self.assertIsNotNone(Review.__doc__)