#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import time

# Sets the max value the iterator() should accept before z "explodes" or goes on until infinity.
infinityBlock = 2

# Helper function that gets the result of z = z*z + c, where z is kept and used again until the absolute value of z becomes greater than 2 or the iterations maxes out at the threshold.
# Returns where it finished, either at a set number or at the supplied threshold value.
def iterator(c, threshold):
    z = c
    for n in range(threshold):
        if abs(z) > infinityBlock:
            return n
        z = z*z + c
    return threshold

# Returns a two dimensional array of a Mandelbrot.
# Applies the iterator() on each complex pair of xArray and yArray and inserts them into a graph.
def mandelbrot1(xMin, xMax, yMin, yMax, width, height, threshold):
    xArray = np.linspace(xMin, xMax, width)
    yArray = np.linspace(yMin, yMax, height)
    graph = np.empty((width, height))

    for i in range(width):
        for q in range(height):
            graph[i, q] = iterator(complex(xArray[i], yArray[q]), threshold)
    return np.rot90(graph)
