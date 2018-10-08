# Introduction
This folder contains four different mandelbrot generator implementations and one "main-file" with user interface. This folder also contain different speed reports, one mandelbrot module, one mandelbrot test file, one art contest image, and one replicator python file.

## Mandelbrot generator (mandelbrot.py)
This is the main file where all the different python implementations can be tested.
Simply run it with:

`python mandelbrot.py <version number>`

where `<version number>` has to be a number from 1-4. The version types is described under:

**1. Python implementation.**
This is the slowest of the four, this only uses some numpy arrays.

**2. Numpy implementation.**
This one is a little bit faster than the python implementation. Here I tried to use vectorized functions.

**3. Numba implementation.**
Much faster than 1. and 2. This one utilizes just-in-time compilation and lower level code for faster computations.

**4. Cython implementation.**
This one creates C code out of the python code. This one is the fastest of the four.

**--help**

You can also run with the flag '--help' instead of a version number.


## Reports (report2.txt, report3.txt, report4.txt)
These reports contain different time comparisons between the implementations. `report4.txt` contain timings of all the four implementations.

## Mandelbrot package (/mandelbrot/setup.py)
To install the mandelbrot package, first run the command

`cd mandelbrot`

to enter the directory where the correct setup file is. Then run

`pip install .`

to install the package. You can now generate a mandelbrot with:

`python`

`>>> import mandelbrot`

`>>> mandelbrot.compute_Mandelbrot(Min, xMax, yMin, yMax, Nx, Ny, threshold, "filename.png"))`

`"filename.png"` and `threshold` are optional.

Default for `threshold` is 1000.

If no filename is supplied, no image will be saved, and it'll just return a Nx × Ny array of the escape times of evenly sampled points in the rectangle [xmin, xmax] × [ymin, ymax].

## Two unit tests (test_mandelbrot.py)
In order to run the two tests, you have to first install 'pytest'. You can do this through Anaconda by simply typing:

`conda install pytest`

Next you can run the two tests with:

`pytest`

## Contest image (contest_image.png)
This is a plot from the generator to enter the contest.

## Good and bad python code (replicator.py)
This file can be run with:

`python replicator.py`

It includes one good and one badly written version of the same function.
