#!/bin/python3.8

# From the c/ dir build with
# ./pybuild.sh ARRAY
# ARRAY should be "int", "char" or "packed" and that's the array library that will be included.
# From there you can use "import rhythm" in any python file that shares a directory with "rhythm.so"
# I will add an option for installing the library to pybuild.sh when the library performs better.

from setuptools import Extension
from setuptools import setup

module = Extension("rhythm", sources=["packed_char_array/array.c", "rhythm.c", "module.c"], extra_compile_args=["-Wall"])

setup(
    name="rhythm",
    version="1.0.0",
    description="An example Python C extension module",
    url="https://github.com/letmeentertainyou/Chartifier",
    author="Lars S",
    author_email="",
    license="MIT",
    classifiers=[
        # I don't have setuptools in my Python2.7, so I am skipping support for it for now.
        #"Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    ext_modules=[module],
)