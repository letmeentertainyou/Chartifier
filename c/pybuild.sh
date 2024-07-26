#!/bin/bash

# This script dynamically creates the rhythm_utils.h and setup.py files depending on which
# version of the array library you ask for [int, char, packed]. This tool does not
# currently have a flag for installing, you can do it manually after running this script once. 
# python3 setup.py install

# Change this path to wherever the .so file is generated on your OS and Python version.
build_path="build/lib.linux-x86_64-cpython-38/rhythm_utils.cpython-38-x86_64-linux-gnu.so"


clean() {
    echo "Removing build artifacts."
    rm *.out > /dev/null 2>&1
    rm *.o > /dev/null 2>&1
    rm *.so > /dev/null 2>&1
    rm -r build > /dev/null 2>&1
}

# This would be changed if there were a second arg for install mode.
if [ $# -ne 1 ]; then
    echo "This script takes exactly one arg."
    exit 1
fi

# When I add a flag for optimization modes I can use a bash variable and plug it into extra_compile_args.
case "$1" in 
    "int")
        array_dir="int_array"
    ;;
    "char")
        array_dir="char_array"
    ;;
    "packed")
        array_dir="packed_char_array"
    ;;
    "clean")
        clean
        exit 1
    ;;
    *)
    echo "The first arg ($1) was not a valid mode."
    exit 1
    ;;
esac

# If I don't clean here then it doesn't compile the code again even though the setup.py file has
# changed, I consider this to be a flaw because I never told it to use the cached build dir.
clean

# The creates the correct rhythm_utils.h file based on which array library you asked for.
echo "Removing old rhythm_utils.h file"
rm rhythm_utils.h > /dev/null 2>&1
echo "Writing new rhythm_utils.h file."

cat << EOF > rhythm_utils.h
#ifndef RHYTHM_UTILS_H_
#define RHYTHM_UTILS_H_
#include "$array_dir/array.h"
Array *rhythm_permutations(int size);
#endif
EOF

# The creates the correct setup.py file based on which array library you asked for.
echo removing old setup.py file
rm setup.py > /dev/null 2>&1
echo "Writing new setup.py file."

cat << EOF > setup.py
from setuptools import Extension
from setuptools import setup

module = Extension("rhythm_utils", sources=["$array_dir/array.c", "rhythm_utils.c", "rhythm_utils_module.c"], extra_compile_args=["-Wall"])

setup(
    name="rhythm_utils",
    version="1.0.0",
    description="An example Python C extension module",
    url="https://github.com/letmeentertainyou/Chartifier",
    author="Lars S",
    author_email="",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    ext_modules=[module],
    py_modules=["rhythm"],
)
EOF

# Runs the 
python3 setup.py build
cp $build_path rhythm_utils.so

# This is optional but it saves me the hassle of typing it out.
./test.py