# -*- coding: utf-8 -*-

from setuptools import setup
from dwdapi.version import version

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='dwd-api',
      version=version,
      author='Markus Stahl',
      author_email='markus.i.sverige@googlemail.com',
      description='api for accessing dwd data',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/noordsestern/dwd-api',
      keywords='dwd mosmix weather',
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent"
      ],
      install_requires=[

      ],
      packages=['dwdapi'],
      )
