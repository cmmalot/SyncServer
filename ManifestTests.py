#!/usr/bin/env python
# encoding: utf-8
"""
ManifestTests.py

Created by Jan Magnusson on 2011-12-18.
Copyright (c) 2011 Jan Magnusson. All rights reserved.
"""

from Manifest import Manifest
import os
import unittest


class ManifestTests(unittest.TestCase):
    def setUp(self):
        self.manifest = Manifest('static_manifest.xml')
        f = open('static_manifest.xml')
        data = f.read()
        self.data = data

    def test_content(self):
        self.assertEqual(self.manifest.find_project(name='platform/build')\
            ['revision'], "81056a1c2bf8d42a9ca70eee90bb04e268dcddb1")

    def test_save(self):
        mf = 'test_manifest.xml'
        if os.path.exists(mf):
            os.remove(mf)
        self.manifest.save(mf)
        self.assertTrue(os.path.exists(mf))

    def test_from_dict(self):
        self.manifest.from_dict(self.manifest.M)
        self.test_content()
        self.test_save()

    def test_from_string(self):
        self.manifest.from_string(self.data)
        self.test_content()

    def test_constructor_with_data(self):
        self.manifest = Manifest(self.data)
        self.test_content

if __name__ == '__main__':
    unittest.main()
