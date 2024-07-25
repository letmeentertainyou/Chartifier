#!/bin/bash

# Clean up the c directory of loose binary files.
echo Removing build artifacts from the c directory.
rm c/*.out > /dev/null 2>&1
rm c/*.o > /dev/null 2>&1
rm c/*.so > /dev/null 2>&1
rm -r c/build > /dev/null 2>&1

# I'm not updating the JS code right now so I'm not bothering to repackage it.
#echo Modifying html, and bundling js modules.
#./scripts/bundler.py Chartifier.html

#echo Copying css.
#cp src/*.css dist/

# Or bundled files get left behind.
#git add --all