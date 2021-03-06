#! /usr/bin/env python
# coding: utf-8

#  __author__ = 'ZhouHeng'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys

if sys.version_info <= (2, 7):
    sys.stderr.write("ERROR: jingyun aliyun python sdk requires Python Version 2.7 or above.\n")
    sys.stderr.write("Your Python Version is %s.%s.%s.\n" % sys.version_info[:3])
    sys.exit(1)

name = "JYAliYun"
version = "0.1.9"
url = "https://github.com/meisanggou/AliYun"
license = "MIT"
author = "meisanggou"
short_description = "Aliyun Service Library"
long_description = """JYAliYun provides interfaces to AliYun Service."""
keywords = "JYAliYun"
install_requires = ["requests >= 2.10.0", "lxml >= 3.7.3"]

setup(name=name,
      version=version,
      author=author,
      author_email="zhouheng@gene.ac",
      url=url,
      packages=["JYAliYun", "JYAliYun/AliYunMNS", "JYAliYun/Tools"],
      license=license,
      description=short_description,
      long_description=long_description,
      keywords=keywords,
      install_requires=install_requires
      )
