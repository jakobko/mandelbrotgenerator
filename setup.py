from distutils.core import setup
from Cython.Build import cythonize

setup(
    name = "mandelbrot_4",
    ext_modules = cythonize("*.pyx"),
)
