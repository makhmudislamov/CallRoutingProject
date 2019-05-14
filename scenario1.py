"""
Scenario 1: One-time route cost check

You have a carrier route list with 100,000 (100K) entries (in arbitrary order) and a single phone number. How quickly can you find the cost of calling this number?

* dictionary
* {key, val} = {routing #, price} 
"""

import sys
import re

def file_to_dict(file_name):
    with open('data/' + file_name, "r") as file:
        price_guide = file.read()
        price_guide = re.split(',|\n', price_guide)
    return price_guide