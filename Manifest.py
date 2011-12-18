#!/usr/bin/env python
# encoding: utf-8
"""
Manifest.py

Created by Jan Magnusson on 2011-12-18.
Copyright (c) 2011 Jan Magnusson. All rights reserved.
"""

from itertools import groupby
from xml.etree.ElementTree import ElementTree
import xml.etree.ElementTree as ET
import os
import re
import sys
import unittest

class Manifest(object):
    def __init__(self, data=None):
        if data:
            self.root = ET.parse(data)
            self.data = data
            self.M = xml2d(self.root)['manifest']

    def fromDict(self, d):
        self.root = ElementTree(d2xml({'manifest':d}))
        self.M = d
        self.data = self._beautify(ET.tostring(self.root.getroot(), encoding='utf-8'))

    def fromText(self, data):
        self.root = ElementTree.parse(data)
        self.M = xml2d(self.root)['manifest']
        self.data = self._beautify(ET.tostring(self.root.getroot(), encoding='utf-8'))

    def save(self, fpath):
        f = open(fpath, 'w')
        f.write(self.data)
        f.close()

    def fromFile(self, f):
        self.root = ElementTree(file=f)
        self.M = xml2d(self.root.getroot())['manifest']
        self.data = self._beautify(ET.tostring(self.root.getroot(), encoding='utf-8'))

    def findProject(self, filter_func=None, name=None, max=1):
        if name and filter_func == None:
            filter_func = lambda x : x['name'] == name
        matches = filter(filter_func, self.M['project'])
        if len(matches) >= 1:
            if max == 1:
                return matches[0]
            if max < len(matches):
                return matches[:max]
            return matches
        return None

    def _beautify(self, data=None):
        if data == None:
            data = self.data
        fields = re.split('(<.*?>)',data)
        indent = 2
        pretty_data = []
        level = 0
        for f in fields:
           if f.strip() == '': continue
           if f[0]=='<' and f[1] != '/':
               pretty_data.append(' '*(level*indent) + f)
               level = level + 1
               if f[-2:] == '/>':
                   level = level - 1
           elif f[:2]=='</':
               level = level - 1
               pretty_data.append(' '*(level*indent) + f)
           else:
               pretty_data.append(' '*(level*indent) + f)
        return "\n".join(pretty_data)

class ManifestTests(unittest.TestCase):
    def setUp(self):
        self.manifest = Manifest()
        self.manifest.fromFile('static_manifest.xml')

    def test_content(self):
        self.assertEqual(self.manifest.findProject(name='platform/build')\
            ['revision'], "81056a1c2bf8d42a9ca70eee90bb04e268dcddb1")

    def test_save(self):
        mf = 'test_manifest.xml'
        if os.path.exists(mf):
            os.remove(mf)
        self.manifest.save(mf)
        self.assertTrue(os.path.exists(mf))

    def test_fromDict(self):
        self.manifest.fromDict(self.manifest.M)
        self.test_content()
        self.test_save()

    def test_save_format(self):
        print self.manifest.data

def xml2d(e):
    """Convert an etree into a dict structure

    @type  e: etree.Element
    @param e: the root of the tree
    @return: The dictionary representation of the XML tree
    """
    def _xml2d(e):
        kids = dict(e.attrib)
        for k, g in groupby(e, lambda x: x.tag):
            g = [ _xml2d(x) for x in g ]
            kids[k]=  g
        return kids
    return { e.tag : _xml2d(e) }

def d2xml(d):
    """convert dict to xml

       1. The top level d must contain a single entry i.e. the root element
       2.  Keys of the dictionary become sublements or attributes
       3.  If a value is a simple string, then the key is an attribute
       4.  if a value is dict then, then key is a subelement
       5.  if a value is list, then key is a set of sublements

       a  = { 'module' : {'tag' : [ { 'name': 'a', 'value': 'b'},
                                    { 'name': 'c', 'value': 'd'},
                                 ],
                          'gobject' : { 'name': 'g', 'type':'xx' },
                          'uri' : 'test',
                       }
           }
    >>> d2xml(a)
    <module uri="test">
       <gobject type="xx" name="g"/>
       <tag name="a" value="b"/>
       <tag name="c" value="d"/>
    </module>

    @type  d: dict
    @param d: A dictionary formatted as an XML document
    @return:  A etree Root element
    """
    def _d2xml(d, p):
        for k,v in d.items():
            if isinstance(v,dict):
                node = ET.SubElement(p, k)
                _d2xml(v, node)
            elif isinstance(v,list):
                for item in v:
                    node = ET.SubElement(p, k)
                    _d2xml(item, node)
            else:
                p.set(k, v)

    k,v = d.items()[0]
    node = ET.Element(k)
    _d2xml(v, node)
    return node

if __name__ == '__main__':
    unittest.main()
