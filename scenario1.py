"""
Scenario 1: One-time route cost check

You have a carrier route list with 100,000 (100K) entries (in arbitrary order) and a single phone number. How quickly can you find the cost of calling this number?

* dictionary
* {key, val} = {routing #, price} 
"""

import sys
import re

def file_to_dict(file_name):
    dict = {}
    with open('data/' + file_name, "r") as file:
        price_guide = file.read()
        price_guide = re.split(',|\n', price_guide)
        i = 0 #counter
        while i < len(price_guide) - 1:
            entry = price_guide[i]
            if entry in dict:
                if dict[entry] > price_guide[i+1]:
                    dict[entry] = price_guide[i+1]
            else:
                if entry[0] == '+':
                    dict[entry] = price_guide[i+1]
            i+=1
    return dict

def call_price(phone_num, price_guide):
    for key,value in price_guide.items():
        if key == phone_num:
            return value
        for i in range(len(phone_num)-1):
            if key[i] == phone_num[i]:
                return value

if __name__ == "__main__":
    path = file_to_dict('route-costs-10.txt')
    target_price = call_price('+86153', path)
    print(target_price)