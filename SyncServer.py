#!/usr/bin/env python
# encoding: utf-8
"""
syncserver.py

Created by Jan Magnusson on 2011-12-17.
Copyright (c) 2011 Jan Magnusson. All rights reserved.
"""

import sys
import os
from twisted.web import xmlrpc, server


class Syncserver(xmlrpc.XMLRPC):
	"""
	Sync server for repo smart-sync.
	"""
	def __init__(self):
		xmlrpc.XMLRPC.__init__(self)

	def xmlrpc_GetApprovedManifest(self, branch=None, target=None):
		print "Looking good"
		if target == None:
			target = "None"
		return [True, "Approved Manifest: %s %s" % (branch, target)]

	def xmlrpc_GetManifest(self, tag=None):
		return [True, "Manifest for tag: %s" % tag]

	def xmlrpc_GetApprovedRevision(self, branch=None, project=None):
		return [True, "Approved Revision for: %s %s" % (branch, project)]

	def xmlrpc_GetRevision(self, tag=None, project=None):
		return [True, "Tagged revision for: %s %s" % (tag, project)]

if __name__ == "__main__":
	from twisted.internet import reactor
	r = Syncserver()
	reactor.listenTCP(8080, server.Site(r))
	reactor.run()