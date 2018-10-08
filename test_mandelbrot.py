from numba import jit

infinityBlock = 2
threshold = 100;

@jit
def iterator(c):
    z = c
    for n in range(threshold):
        if abs(z) > infinityBlock:
            return n
        z = z*z + c
    return threshold

def checkOutside(xMin, xMax, yMin, yMax):
    if iterator(complex(xMin, yMin)) == threshold or iterator(complex(xMax, yMax)) == threshold:
        return 1
    else:
        return 0

def test_outside():
    assert checkOutside(1.2, 1.5, -1.2, -1.1) == 0

def test_inside():
    assert checkOutside(-1.7, 0.1, -0.9, 0.345) == 1
