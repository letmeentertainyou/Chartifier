#!/bin/bash

echo Modifying html, and bundling js modules.
./scripts/remove_script_tags.py Chartifier.html

echo Copying css.
cp src/*.css dist/

