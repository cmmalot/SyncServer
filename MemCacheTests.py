#!/usr/bin/env python
# encoding: utf-8
"""
MemCacheTests.py

Created by Jan Magnusson on 2012-01-09.
Copyright (c) 2012 Jan Magnusson. All rights reserved.
"""

import unittest
import MemCache


class MemCacheTests(unittest.TestCase):
    DATA = { '1' : "one",
             '2' : "two",
             '3' : "three",
             '4' : "four",
             '5' : "five",
             '6' : "six",
             '7' : "seven",
             '8' : "eight",
             '9' : "nine",
             '10' : "huge" * (2^16)}
    ERROR_KEY = 'no such key'

    def setUp(self):
        self.memcache = MemCache.MemCache(50)
        self.test_store()

    def test_store(self):
        for (key, value) in iter(MemCacheTests.DATA.items()):
            self.memcache.store(key, value)

    def test_get_ok(self):
        """docstring for test_get"""
        for (key, value) in iter(MemCacheTests.DATA.items()):
            self.assertEqual(value, self.memcache.get(key),
            'Actual value for key %s differs from expected value' % key)
            
    def test_get_nok(self):
        """docstring for test_get_nok"""
        self.assertRaises(KeyError, self.memcache.get, 
                              MemCacheTests.ERROR_KEY)

    def test_get_refresh(self):
        """docstring"""
        oldest = self.memcache.key_at_index(0)
        last_index = self.memcache.size - 1
        newest = self.memcache.key_at_index(last_index)
        self.memcache.get(oldest)
        self.assertIs(oldest, self.memcache.key_at_index(last_index),
            "Oldest not newest after get")
        self.assertIs(newest, self.memcache.key_at_index(last_index - 1),
            "Newest not second newest after get")

if __name__ == '__main__':
    unittest.main()
