import numpy

def load_file(file_path):
    x, y, dy = numpy.loadtxt(file_path, unpack=True)
    x *= 10
    return x, y, dy