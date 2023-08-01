#!/usr/bin/python3
"""Test Kwags"""

from models.base_model import BaseModel

Kwags_test = {'name':"California"}

test_base_kwags = BaseModel(**Kwags_test)

print(test_base_kwags.name)

print(test_base_kwags)

test_base_kwags = test_base_kwags.delete()

if test_base_kwags:
    print(test_base_kwags)
else:
    print("Success")
