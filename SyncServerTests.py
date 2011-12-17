#!/usr/bin/env python
# encoding: utf-8
"""
SyncServerTests.py

Created by Jan Magnusson on 2011-12-17.
Copyright (c) 2011 Jan Magnusson. All rights reserved.
"""

import unittest
import xmlrpclib

class SyncServerTests(unittest.TestCase):
	branch = "branch"
	target = "target"
	tag = "1.0.A.0.1"
	
	def setUp(self):
		self.server = xmlrpclib.Server('http://localhost:8080')

	def test_GetApprovedManifest(self):
		(success, txt) = self.server.GetApprovedManifest(self.branch)
		self.assertTrue(success)
		(success, txt) = self.server.GetApprovedManifest(self.branch, self.target)
		self.assertTrue(success)
		
    
if __name__ == '__main__':
	unittest.main()