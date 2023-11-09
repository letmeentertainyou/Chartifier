#!/bin/python3

"""This script only runs from the root directory because it expects to be run as a pre-commit hook.
Use this command in the root dir.
$ ./scripts/bundler.py

In order to test this project in a browser I have written js code that does not use the 
import, export or require statements. Unfortunately it seems that js bundlers depend on
import/export statements and using something like WebPack would require recompiling the code
because I can render any changes I make. So I wrote my own bundler that works with browser
compatible js from the start. 

I also prefer having semi readable code in the dist directory because I find obfuscated code goes
against the idea of open source anyways.
"""

from sys import argv
from typing import List


def js_module_remover(filename: str) -> List[str]:
    """Strips te modules from the HTML, and writes it to source. Then returns a list
    of the modules for the next step."""

    with open(f"src/{filename}", "r", encoding="UTF-8") as tmpfile:
        file = tmpfile.readlines()

    html_out: List = []
    modules: List = []
    for index, line in enumerate(file):
        if index == len(file) - 1:
            html_out.append('<script src="main.js"></script>\n')

        if "<script" not in line:
            html_out.append(line)
        else:
            module = line.split('"')[1]
            if module != "js/devTools.js":
                modules.append(line.split('"')[1])

    with open(f"dist/{filename}", "w", encoding="UTF-8") as tmpfile:
        tmpfile.writelines(html_out)

    return modules


def js_bundler(modules: List[str]) -> None:
    """Combines all of the js modules provided by the above function into a single
    main.js file. This function removes empty new lines and any any lines that only
    contain comments from the js_out. Any lines that end in a comment are ignored by
    this version."""

    js_out: List[str] = []
    multiline_comment: bool = False
    for script in modules:
        with open(f"src/{script}", "r", encoding="UTF-8") as tmpfile:
            lines: List[str] = tmpfile.readlines()

        js_out.append(f"/* {script[3:-3].upper()} */\n")

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

            js_out.append(line)

    with open("dist/main.js", "w", encoding="UTF-8") as tmpfile:
        tmpfile.writelines(js_out)


if __name__ == "__main__":
    modules = js_module_remover(argv[1])
    js_bundler(modules)
