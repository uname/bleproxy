#-*- coding: utf-8 -*-
from distutils.core import setup
import py2exe

setup( zipfile=None,
       windows=[{"script":"main.py", "icon_resources":[(1, "resource/icons/app/logo1.ico")]}],
	   options={"py2exe":{"compressed":2, "bundle_files":1,
                          "includes":["sip", "PyQt4.QtGui", "PyQt4.QtCore",
                                      "serial",
                                      "google.protobuf.internal", "pkg_resources", "google.protobuf"],
                          "dll_excludes": ["msvcm90.dll", "msvcp90.dll", "msvcr90.dll"] }})