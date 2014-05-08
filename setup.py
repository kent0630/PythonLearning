#!/usr/bin/python

from distutils.core import setup
import py2exe

setup(
    version = "0.5.0",
    description = "py2exe sample script",
    name = "py2exe samples",
	# windows = ["simple.py"],
    console = [{"script":"mailtest.py", 
                "icon_resources":[(1, "../res/icon.ico")]}],
	zipfile = None,
	options={"py2exe" : {"compressed": 1,
						 "optimize": 2,
						 "bundle_files": 1, 
						 "includes" : ['sip','PyQt4._qt']}}
    )
