# https://oj.leetcode.com/problems/lru-cache/
# 17 / 17 test cases passed.
# Design and implement a data structure for Least Recently Used (LRU) cache.
# It should support the following operations: get and set.
#
# get(key) - Get the value (will always be positive) of the key
# if the key exists in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently
# used item before inserting a new item.


class LRUCache:

    def __init__(self, capacity):
        ''' Initialize the cache
        @param capacity, an integer
        '''
        self.max_capacity = capacity
        self.count = 0
        self.cache = {}
        self.history = []

    def get(self, key):
        ''' Get cache value using key
        @return an integer
        '''
        if self.cache.has_key(key):
            self.history.remove(key)
            self.history.append(key)
            return self.cache[key]
        return -1

    def set(self, key, value):
        ''' Set cache value
        @param key, an integer
        @param value, an integer
        @return nothing
        '''
        # not found
        if self.get(key) == -1:
            if self.count == self.max_capacity:
                # if full delete first
                del self.cache[self.history.pop(0)]
                self.cache[key] = value
                self.history.append(key)
            else:
                self.cache[key] = value
                self.history.append(key)
                self.count += 1
        else:
            # already there, just change the val
            self.cache[key] = value

    def print_all(self):
        ''' For debugging purpose '''
        print self.cache
        print self.history


if __name__ == '__main__':
    # test
    lru_cache = LRUCache(3)
    lru_cache.set(1,1)
    lru_cache.set(2,2)
    lru_cache.set(3,3)
    lru_cache.set(4,4)
    assert lru_cache.get(4) == 4
    assert lru_cache.get(3) == 3
    assert lru_cache.get(2) == 2
    assert lru_cache.get(1) == -1
    lru_cache.set(5,5)
    assert lru_cache.get(1) == -1
    assert lru_cache.get(2) == 2
    assert lru_cache.get(3) == 3
    assert lru_cache.get(4) == -1
    assert lru_cache.get(5) == 5

    # # test
    lru_cache = LRUCache(2)
    lru_cache.set(2,1)
    lru_cache.set(2,2)
    result = lru_cache.get(2)
    lru_cache.set(1,1)
    lru_cache.set(4,1)
    result = lru_cache.get(2)

    # # test first
    lru_cache = LRUCache(2)
    lru_cache.set(2,1)
    lru_cache.set(1,1)
    assert lru_cache.get(2) == 1
    lru_cache.set(4,1)
    assert lru_cache.get(1) == -1
    assert lru_cache.get(2) == 1

    # test second
    lru_cache = LRUCache(1)
    lru_cache.set(2, 1)
    assert lru_cache.get(2) == 1
    lru_cache.set(3, 2)
    assert lru_cache.get(2) == -1
    assert lru_cache.get(3) == 2

    # test third
    lru_cache = LRUCache(10)
    lru_cache.set(10,13)
    lru_cache.set(3,17)
    lru_cache.set(6,11)
    lru_cache.set(10,5)
    lru_cache.set(9,10)
    result = lru_cache.get(13)
    lru_cache.set(2,19)
    result = lru_cache.get(2)
    result = lru_cache.get(3)
    lru_cache.set(5,25)
    result = lru_cache.get(8)
    lru_cache.set(9,22)
    lru_cache.set(5,5)
    lru_cache.set(1,30)
    result = lru_cache.get(11)
    lru_cache.set(9,12)
    result = lru_cache.get(7)
    result = lru_cache.get(5)
    result = lru_cache.get(8)
    result = lru_cache.get(9)
    lru_cache.set(4,30)
    lru_cache.set(9,3)
    result = lru_cache.get(9)
    result = lru_cache.get(10)
    result = lru_cache.get(10)
    lru_cache.set(6,14)
    lru_cache.set(3,1)
    result = lru_cache.get(3)
    lru_cache.set(10,11)
    result = lru_cache.get(8)
    lru_cache.set(2,14)
    result = lru_cache.get(1)
    result = lru_cache.get(5)
    result = lru_cache.get(4)
    lru_cache.set(11,4)
    lru_cache.set(12,24)
    lru_cache.set(5,18)
    result = lru_cache.get(13)
    lru_cache.set(7,23)
    result = lru_cache.get(8)
    result = lru_cache.get(12)
    lru_cache.set(3,27)
    lru_cache.set(2,12)
    result = lru_cache.get(5)
    lru_cache.set(2,9)
    lru_cache.set(13,4)
    lru_cache.set(8,18)
    lru_cache.set(1,7)
    result = lru_cache.get(6)
    lru_cache.set(9,29)
    lru_cache.set(8,21)
    result = lru_cache.get(5)
    lru_cache.set(6,30)
    lru_cache.set(1,12)
    result = lru_cache.get(10)
    lru_cache.set(4,15)
    lru_cache.set(7,22)
    lru_cache.set(11,26)
    lru_cache.set(8,17)
    lru_cache.set(9,29)
    result = lru_cache.get(5)
    lru_cache.set(3,4)
    lru_cache.set(11,30)
    result = lru_cache.get(12)
    lru_cache.set(4,29)
    result = lru_cache.get(3)
    result = lru_cache.get(9)
    result = lru_cache.get(6)
    lru_cache.set(3,4)
    result = lru_cache.get(1)
    result = lru_cache.get(10)
    lru_cache.set(3,29)
    lru_cache.set(10,28)
    lru_cache.set(1,20)
    lru_cache.set(11,13)
    result = lru_cache.get(3)
    lru_cache.set(3,12)
    lru_cache.set(3,8)
    lru_cache.set(10,9)
    lru_cache.set(3,26)
    result = lru_cache.get(8)
    result = lru_cache.get(7)
    result = lru_cache.get(5)
    lru_cache.set(13,17)
    lru_cache.set(2,27)
    lru_cache.set(11,15)
    result = lru_cache.get(12)
    lru_cache.set(9,19)
    lru_cache.set(2,15)
    lru_cache.set(3,16)
    result = lru_cache.get(1)
    lru_cache.set(12,17)
    lru_cache.set(9,1)
    lru_cache.set(6,19)
    result = lru_cache.get(4)
    result = lru_cache.get(5)
    result = lru_cache.get(5)
    lru_cache.set(8,1)
    lru_cache.set(11,7)
    lru_cache.set(5,2)
    lru_cache.set(9,28)
    result = lru_cache.get(1)
    lru_cache.set(2,2)
    lru_cache.set(7,4)
    lru_cache.set(4,22)
    lru_cache.set(7,24)
    lru_cache.set(9,26)
    lru_cache.set(13,28)
    lru_cache.set(11,26)
