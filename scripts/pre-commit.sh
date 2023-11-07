#!/bin/bash

echo Modifying html, and bundling js modules.
./scripts/bundler.py Chartifier.html

echo Copying css.
cp src/*.css dist/

# Or bundled files get left behind.
git add --all