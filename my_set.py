#!python

from hashtable import HashTable

class Set(object):

    def __init__(self, elements=None):
        self.hashtable = HashTable()
        self.size = 0
        if elements is not None:
            for element in elements:
                self.add(element)


    def contains(self, element):
        """Returns a boolean indicating whether element is in this set
        Time Complexity: O(1) >> hashtable lookup is a const operation on average case
        Space Complexity: O(n) >> n is a bucket size.
        """
        if not self.hashtable:
            raise ValueError('Empty Hashtable')
        else:
            return self.hashtable.contains(element)

    def add(self, element):
        """Adds element to this set, if not present already
        Time Complexity: O(1) >> set method of hastable is const time
        Space Complexity: O(1) >> one new space is created for new element
        """
        if self.contains(element) is True:
            return 
        else:
            self.hashtable.set(element, None)
            self.size += 1
    
    def remove(self, element):
        """Removes element from this set, if present, or else raise KeyError
        Time Complexity: O(n) >> delete method of hastable is const time
        Space Complexity: O(n) >> 
        """
        if self.contains(element) is False:
            raise KeyError('Element does not exist')
        else:
            self.hashtable.delete(element)
            self.size -= 1

    def union(self, other_set):
        """Returns a new set that is the union of this set and other_set
        Time Complexity: O(n+m) >> two loops >> two different hashtables and each has own length 
        Space Complexity: O(n+m) >> creating space for new each element one by one. n + m  
        """
        united_set = Set()
        # adding elements of self to united_set
        for element in self.hashtable.keys():
            united_set.add(element)
        # adding elements of other_set to united_set
        for element in other_set.hashtable.keys():
            united_set.add(element)
        
        return united_set


    def intersection(self, other_set):
        """Returns a new set that is the intersection of this set and other_set
        Time Complexity: O(n) >> travaersing through the hashtable to collect and compare the elements 
        Space Complexity: O(n) >> creating space for new each element one by one
        """

        inter_set = Set()
        # smaller set has to be iterated and its elements should be compared to larger set
        if self.size > other_set.size:
            big_set = self
            small_set = other_set
        else:
            big_set = other_set
            small_set = self

        for element in small_set.hashtable.keys():
            if big_set.hashtable.contains(element) is True:
                inter_set.add(element)
        
        return inter_set
    
    def difference(self, other_set):
        """Returns a new set that is the difference of this set and other_set
        Time Complexity: O(n) >> travaersing through the hashtable to collect and compare the elements 
        Space Complexity: O(n) >> creating space for new each element one by one
        """ 
        differ_set = Set()
        for element in self.hashtable.keys():  
            if not other_set.hashtable.contains(element):
                differ_set.add(element)
        
        for element in other_set.hashtable.keys():
            if not self.hashtable.contains(element):
                differ_set.add(element)

        return differ_set
        
    
    def is_subset(self, other_set):
        """Returns a boolean indicating whether other_set is a subset of this set
        Time Complexity: O(n) >> travaersing through the hashtable to collect and compare the elements 
        Space Complexity: O(n) >> creating space for new each element one by one
        """
         # smaller set has to be iterated and its elements should be compared to larger set
        if self.size > other_set.size:
            big_set = self
            small_set = other_set
        else:
            big_set = other_set
            small_set = self

        for element in small_set.hashtable.keys():
            if big_set.hashtable.contains(element) is True:
                return True
            else:
                return False
        


if __name__ == '__main__':
    pass


    
