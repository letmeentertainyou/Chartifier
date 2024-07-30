#!/bin/bash

# This script dynamically creates the rhythm_utils.h and setup.py files depending on which
# version of the array library you ask for [int, char, packed]. This tool does not
# currently have a flag for installing, you can do it manually after running this script once. 
# python3 setup.py install

# Change this path to wherever the .so file is generated on your OS and Python version.
build_path="build/lib.linux-x86_64-cpython-38/rhythm_utils.cpython-38-x86_64-linux-gnu.so"

# The three array libraries you can build with.
modes=("int" "char" "packed")

# Removes the build artifacts.
clean() {
    echo "Removing build artifacts."
    rm *.out > /dev/null 2>&1
    rm *.o > /dev/null 2>&1
    rm *.so > /dev/null 2>&1
    rm setup.py > /dev/null 2>&1
    rm rhythm_utils.h > /dev/null 2>&1
    rm -r build > /dev/null 2>&1
}

# This would be changed if there were a second arg for install mode.
if [ $# -ne 1 ]; then
    echo "This script takes exactly one arg."
    exit 1
elif [ $1 == "clean" ]; then
    clean
    exit 1
elif [[ " ${modes[@]} " =~ " $1 " ]]; then
    clean  # If I don't clean here then it doesn't compile the code again.

    # Replace ARRAY_DIR in the template with the requested location.
    sed "s/ARRAY_DIR/${1}_array/g" templates/rhythm_utils > rhythm_utils.h
    sed "s/ARRAY_DIR/${1}_array/g" templates/setup > setup.py

    # Build
    python3 setup.py build
    cp $build_path rhythm_utils.so
    
    # Run
    ./test.py
else
    echo "The first arg ($1) was not a valid mode."
    exit 1
fi