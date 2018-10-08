#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import time

# Imports all the different mandelbrot implementations.
from mandelbrot_1 import mandelbrot1
from mandelbrot_2 import mandelbrot2
from mandelbrot_3 import mandelbrot3
from mandelbrot_4 import mandelbrot4

threshold = 100
version = 0

# Finds and saves the plot from the user inserted values.
def findPlot(version, filename, colorChoice, xMinIn, xMaxIn, yMinIn, yMaxIn, widthIn, heightIn):
    colorMapInput = "bone"
    if colorChoice == "1":
        colorMapInput = "bone"
    elif colorChoice == "2":
        colorMapInput = "magma"
    elif colorChoice == "3":
        colorMapInput = "flag"

    height = int(heightIn)
    width = int(widthIn)
    xMin = float(xMinIn)
    xMax = float(xMaxIn)
    yMin = float(yMinIn)
    yMax = float(yMaxIn)

    if version == "1":
        graph = mandelbrot1(xMin, xMax, yMin, yMax, width, height, threshold)
        plt.imsave(filename, graph, cmap=colorMapInput)
        plt.close()
    elif version == "2":
        graph = mandelbrot2(xMin, xMax, yMin, yMax, width, height, threshold)
        plt.imsave(filename, graph, cmap=colorMapInput)
        plt.close()
    elif version == "3":
        graph = mandelbrot3(xMin, xMax, yMin, yMax, width, height, threshold)
        plt.imsave(filename, graph, cmap=colorMapInput)
        plt.close()
    elif version == "4":
        graph = mandelbrot4(xMin, xMax, yMin, yMax, width, height, threshold)
        plt.imsave(filename, graph, cmap=colorMapInput)
        plt.close()

# User Interface getting inputs from the user.
def ui():
    print("")
    print("Welcome to the mandelbrot generator!")
    print("You have chosen to use version: {}".format(version))

    if version == "1":
        print("Version 1 utilizes a python implementation, and is the slowest.")
    elif version == "2":
        print("Version 2 utilizes a numpy implementation, and is a little bit faster than version 1, but slower than version 3.")
    elif version == "3":
        print("Version 3 utilizes a just-in-time compilator Numba. This is much faster than the two first.")
    elif version == "4":
        print("Version 4 is a cython implementation that utilizes C code to run much more optimized.")

    print("")
    print("Enter values in the following steps to generate a plot:")
    print("Plane to render, xMin (number) (suggestion: -2):")
    xMin = input()
    print("Plane to render, xMax (number) (suggestion: 1):")
    xMax = input()
    print("Plane to render, yMin (number) (suggestion: -1.5):")
    yMin = input()
    print("Plane to render, yMax (number) (suggestion: 1.5):")
    yMax = input()
    print("Resolution, width (number) (sugestion: 1000):")
    width = input()
    print("Resolution, height (number) (suggestion: 1000):")
    height = input()
    print("Color choice (enter 1, 2 or 3):")
    colorChoice = input()
    print("Filename (example: filename.png):")
    filename = input()
    print("Your plot will now be rendered and saved as '{}'.".format(filename))
    print("Loading...")
    time1 = time.time()
    findPlot(version, filename, colorChoice, xMin, xMax, yMin, yMax, width, height)
    time2 = time.time() - time1
    print("Your plot is now finished.")
    print("Finished in: {} seconds".format(time2))

# Assumes correct input from the user.
if (sys.argv[1] == "--help"):
    print("")
    print("Use the command 'python mandelbrot.py <version>'")
    print("<version> can the numbers 1, 2 or 3.")
    print("Version 1 is the python implementation.")
    print("Version 2 is the numpy implementation.")
    print("Version 3 is the numba implementation.")
    print("Version 4 is the cython implementation.")
    print("")
else:
    version = sys.argv[1]
    ui()
