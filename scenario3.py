"""
Scenario 3: Multiple long carrier route lists

You have 5 carrier route lists, each with 10,000,000 (10M) entries (in arbitrary order) and a list of 10,000 phone numbers. How can you speed up your route cost lookup solution to handle this larger dataset?
"""

import sys
import os
import glob
from time import time

class TrieNode(object):
    def __init__(self, data=None):
        self.data = data
        self.price = None
        self.dict = {}

class Trie(object):
    def __init__(self, route_prices):
        self.root = TrieNode()
        for file in route_prices:
            self.make_trie(file)
    
    def make_trie(self, route_prices):
        for line in open(route_prices):
            current_node = self.root
            entry = line.split(",")
            route = entry[0]
            price = entry[1]
            price = float(price.strip("\n"))
            for num in route:
                if num not in current_node.dict:
                    current_node.dict[num] = TrieNode(num)
                current_node = current_node.dict[num]
            if current_node.price is not None:
                if current_node.price > price:
                    current_node.price = price
            else:
                current_node.price = price

    def write_file(self, phone_numbers):
        for phone_num in open(phone_numbers):
            current_node = self.root
            answer_price = float('inf')
            for num in phone_num:
                if current_node.price is not None:
                    answer_price = min(answer_price, current_node.price)
                if num in current_node.dict:
                    current_node = current_node.dict[num]
                else:
                    break
            phone_num = phone_num.strip('\n')
            if answer_price != float('inf'):
                with open("output2.txt", "a+") as file:
                    file.write(phone_num + ", " + str(answer_price) + '\n')
            else:
                with open("output2.txt", "a+") as file:
                    file.write(phone_num + ", 0 \n")

if __name__ == "__main__":
    # loading route cost and time spent
    start = time()
    price_guide = glob.glob('data/route-costs-*.txt')
    end = time()
    total = end - start
    print("Time for loading route cost data: {total} seconds")
    # building a trie and time spent
    start = time()
    trie_for_all = Trie(price_guide)
    end = time()
    total = end - start
    print('TRIE ALL DONE')
    print("Time for building the trie: {total} seconds")
    # loading numbers and time spent
    start = time()
    phone_numbers = ('data/phone-numbers-100.txt')
    end = time()
    total = end - start
    print("Time for loading phone numbers data: {total} seconds")
    # writing the results to a file and time spent
    start = time()
    trie_for_all.write_file(phone_numbers)
    end = time()
    total = end - start
    print("Time for writing data to a file: {total} seconds")