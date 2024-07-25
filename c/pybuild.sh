#!/bin/bash

# This script dynamically creates the rhythm.h file needed depending on which
# array package you want. The setup.py scripts for each different array package
# are stored in the same dir as array.c/array.h. I would like to update this script
# to dynamically create setup.py too but that's going to be a bit more effort.

build_path="build/lib.linux-x86_64-cpython-38/rhythm.cpython-38-x86_64-linux-gnu.so"

if [ $# -ne 1 ]; then
    echo "This script takes exactly one arg."
    exit 1
fi

case "$1" in 
    "int")
        package='#include "int_array/array.h"'
        setup="int_array/setup.py"
    ;;
    "char")
        package='#include "char_array/array.h"'
        setup="char_array/setup.py"
    ;;
    "packed")
        package='#include "packed_char_array/array.h"'
        setup="packed_char_array/setup.py"
    ;;
    "clean")
        rm *.out > /dev/null 2>&1
        rm *.o > /dev/null 2>&1
        rm *.so > /dev/null 2>&1
        rm -r build > /dev/null 2>&1
        exit 1
    ;;
    *)
    echo "The first arg ($1) was not a valid mode."
    exit 1
    ;;
esac

echo removing old rhythm.h file
rm rhythm.h

# The creates the correct rhythm.h file based on which array library you asked for.
cat << EOF > rhythm.h
#ifndef RHYTHM_H_
#define RHYTHM_H_
$package
Array *rhythm_permutations(int size);
#endif
EOF

python3 $setup build
mv $build_path rhythm.so