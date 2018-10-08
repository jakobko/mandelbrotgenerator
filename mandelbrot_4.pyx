#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import time
import cython

# Sets the max value the iterator() should accept before z "explodes" or goes on until infinity. I set it to 4.0 here, as 2.0 created a smaller circle plot.
cdef:
    double infinityBlock = 4.0

# Helper function that gets the result of z = z*z + c, where z is kept and used again until the absolute value of z becomes greater than 2 or the iterations maxes out at the threshold.
# Returns where it finished, either at a set number or at the supplied threshold value.
cdef int iterator(double creal, double cimag, int threshold):

    # To make complex numbers work I have to define real and imaginary pairs for xArray and yArray.
    cdef:
        double real1 = creal
        double imag1 = cimag
        double real2
        double imag2
        int n

    for n in range(threshold):
        # Multiply to create the the initial complex number result real2 and imag2. Makes an absolute value version of the complex number.
        real2 = real1 * real1
        imag2 = imag1 * imag1

        # Checks to see if the complex number real2 + imag2 is greater than the infinityBlock.
        if real2 + imag2 > infinityBlock:
            # Return the amount of iterations
            return n

        # If its not above the infinityBlock create new set of real and imaginary numbers based on the function z = z * z + c. The complex number i^2 = -1.
        imag1 = 2 * real1 * imag1 + cimag
        real1 = real2 - imag2 + creal;
    return threshold

cpdef mandelbrot4(double xMin, double xMax, double yMin, double yMax, int width, int height, int threshold):
    cdef:
        # Creates double arrays and one multi dimensional int array.
        # Initializes i and q for use in the for-loop
        double[:] xArray = np.linspace(xMin, xMax, width)
        double[:] yArray = np.linspace(yMin, yMax, height)
        int[:,:] graph = np.empty((width, height), dtype=np.int32)
        int i, q

    for i in range(width):
        for q in range(height):
            graph[i, q] = iterator(xArray[i], yArray[q], threshold)

    return np.rot90(graph)
