#!/usr/bin/python3
""" Unittest for State class """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import pycodestyle


class test_state(test_basemodel):
    """ Test cases for State class """

    def __init__(self, *args, **kwargs):
        """ Init method """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ Test for name type """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_docs(self):
        """ Test for doc """
        self.assertIsNotNone(State.__doc__)