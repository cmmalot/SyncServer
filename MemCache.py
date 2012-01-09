# encoding: utf-8
"""
MemCache.py

Created by Jan Magnusson on 2012-01-09.
Copyright (c) 2012 Jan Magnusson. All rights reserved.
"""

import os


class MemCache:
    def __init__(self, size=1):
        self.maxsize = size
        self.items = []
        self.item_data = {}

    def store(self, key=None, value=None):
        if key in self.items:
            return
        if self.size <= self.maxsize:
            self.items.append(key)
            self.item_data[key] = value
        else:
            self.remove(self.items[0])
            self.items.append(key)
            self.item_data[key] = value

    def get(self, key=None):
        if key in self.items:
            self.refresh(key)
            return self.item_data[key]
        else:
            raise KeyError('Key %s does not exist' % key)

    def remove(self, key=None):
        if key in self.items:
            self.items.remove(key)
            del self.item_data[key]

    def refresh(self, key=None):
        if key in self.items:
            if self.items.index(key) == (self.size -1):
                return
            self.items.remove(key)
            self.items.append(key)

    def clear(self):
        """docstring for clear"""
        self.__init__(self.size)

    def index(self, key=None):
        """docstring for index"""
        return self.items.index(key)

    def key_at_index(self, index):
        """docstring"""
        return self.items[index]

    def size():
        doc = "The size property."
        def fget(self):
            return len(self.items)
        return locals()
    size = property(**size())

if __name__ == '__main__':
    unittest.main()