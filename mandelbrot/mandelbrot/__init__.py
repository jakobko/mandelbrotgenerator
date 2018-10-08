#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

# This version uses the jit decoration, speeding up the computation further.
from numba import jit

# Sets the max value the iterator() should accept before z "explodes" or goes on until infinity.
infinityBlock = 2

# Helper function that gets the result of z = z*z + c, where z is kept and used again until the absolute value of z becomes greater than 2 or the iterations maxes out at the threshold.
# Returns where it finished, either at a set number or at the supplied threshold value.
@jit
def iterator(c, threshold):
    z = c
    for n in range(threshold):
        if abs(z) > infinityBlock:
            return n
        z = z*z + c
    return threshold

# Returns a two dimensional array of a Mandelbrot.
# Applies the iterator() on each complex pair of xArray and yArray and inserts them into a graph.
@jit
def mandelbrot3(xMin, xMax, yMin, yMax, width, height, threshold):
    xArray = np.linspace(xMin, xMax, width)
    yArray = np.linspace(yMin, yMax, height)
    graph = np.empty((width, height))

    # Here I used the non-vectorized version as created in mandelbrot_1.py or assignment 4.1.
    for i in range(width):
        for q in range(height):
            graph[i, q] = iterator(complex(xArray[i], yArray[q]), threshold)
    return np.rot90(graph)

def compute_Mandelbrot(xMin, xMax, yMin, yMax, Nx, Ny, threshold=1000, filename=None):
    if filename == None:
        return mandelbrot3(xMin, xMax, yMin, yMax, Nx, Nx, threshold)
    else:
        graph = mandelbrot3(xMin, xMax, yMin, yMax, Nx, Nx, threshold)
        plt.imsave(filename, graph, cmap="magma")
        plt.close()
