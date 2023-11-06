#!/bin/python3

"""This saves me the headache of having to Webpack my html. The downside is that it
removes every single <script> tag from the input html file. So this solution will not
work with more complicated projects and I will have to learn more about Webpack then. """

from sys import argv

with open(f"src/{argv[1]}", "r", encoding="UTF-8") as tmpfile:
    file = tmpfile.readlines()

output = []
for index, line in enumerate(file):
    if index == len(file) - 1:
        output.append('<script src="main.js"></script>\n')

    if "<script" not in line:
        output.append(line)

with open(f"dist/{argv[1]}", "w", encoding="UTF-8") as tmpfile:
    tmpfile.writelines(output)
