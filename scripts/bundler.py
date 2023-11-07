#!/bin/python3

"""
In order to test this project in a browser I have written js code that does not use the 
import, export or require statements. I cannot use webpack without explicitly exporting all
of my functions and that ruins my browser support. So instead I am writing a this script to
simply combine all of js my files together in the correct order, and strip away the comments.

I also prefer having semi readable code in the dist/ dir because I find obfuscated code goes
against the idea of open source.
"""

# This script should read the html file, and grab all the script tags
# So that  the modules list is generated dynamically, then each module that
# gets added to the html page will automatically get added to this script
# If I keep everything that is not part of the website in devTools.js then
# I can limit the complexity of this task.
# Also pattern matching.
modules = ["random", "tools", "musicTheory", "rhythm", "main"]

output = []
multiline_comment = False
for script in modules:
    with open(f"src/js/{script}.js", "r", encoding="UTF-8") as tmpfile:
        lines = tmpfile.readlines()

    for line in lines:
        if line.lstrip()[0:2] == "/*":
            multiline_comment = True

        if "*/" in line:
            multiline_comment = False
            continue

        if multiline_comment:
            continue

        if line == "\n":
            continue

        if line.lstrip()[0:2] == "//":
            continue

        output.append(line)

with open("dist/main.js", "w", encoding="UTF-8") as tmpfile:
    tmpfile.writelines(output)
