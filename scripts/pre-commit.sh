#!/bin/bash

# This file won't actually run from the scripts directory, It is stored outside of the
# repo in .git/hooks

echo Modifying html.
./scripts/remove_script_tags.py Chartifier.html

echo Copying css.
cp src/*.css dist/

echo Bundling all JS modules into one file.
./scripts/bundler.py
