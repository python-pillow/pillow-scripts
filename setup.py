#!/usr/bin/env python
from setuptools import setup
import glob

def _read(file):
    with open(file, 'rb') as fp:
        return fp.read()

setup(name='pillow-scripts',
      version='5.0.0',
      description='Python Imaging Library (Fork) Scripts',
      long_description=_read('README.rst').decode('utf-8'),
      author='Alex Clark (Fork Author)',
      author_email='aclark@aclark.net',
      url='https://github.com/python-pillow/pillow-scripts/',
      classifiers=[
          "Development Status :: 6 - Mature",
          "Topic :: Multimedia :: Graphics",
          "Topic :: Multimedia :: Graphics :: Capture :: Digital Camera",
          "Topic :: Multimedia :: Graphics :: Capture :: Screen Capture",
          "Topic :: Multimedia :: Graphics :: Graphics Conversion",
          "Topic :: Multimedia :: Graphics :: Viewers",
          "License :: Other/Proprietary License",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: Implementation :: CPython",
          "Programming Language :: Python :: Implementation :: PyPy",
      ],
      python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*",
      scripts=glob.glob("Scripts/*.py"),
      keywords=["Imaging", ],
      license='Standard PIL License',
      zip_safe=False
      )
