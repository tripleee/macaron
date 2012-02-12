#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Project:
# Module:
from distutils.core import setup
import sys
if sys.version_info < (2, 5):
    raise NotImplementedError("Sorry, you need at least Python 2.5 to use Macaron.")

import macaron

setup(
    name                = "macaron",
    version             = macaron.__version__,
    description         = "Very simple O/R mapper for SQLite3 in small applications",
    long_description    = macaron.__doc__,
    author              = macaron.__author__,
    author_email        = "macaron@biokids.org",
    url                 = "http://github.com/nobrin/macaron",
    py_modules          = ["macaron"],
    scripts             = ["macaron.py"],
    license             = "MIT",
    platforms           = "any",
    classifiers         = [
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Database",
        "Topic :: Database :: Front-Ends",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
)
