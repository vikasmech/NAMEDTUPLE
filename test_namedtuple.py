import pytest
import random
from namedtuple import *
import os
import inspect
import re
import math





def test_gen_profiles_tuples():
    profiles = fake_profile_generator(50)
    assert len(profiles) == 50, "Something wrong with the  generate_profiles_using_namedtuple function."
    

def test_gen_profiles_dict():
    profiles = generate_profiles_using_dictionary(50)
    assert len(profiles) == 50, "Something wrong with the generate_profiles_using_dictionary function."
  
test_gen_profiles_dict()