import numpy as np


def sin_function(angle):
    """Returns the sin of angle.
    angle should be given in radians"""
    return np.sin(angle)


def int_add_function(var1, var2, allow_casting=False):
    """function to add integers and only integers
    if allow_casting is True the variables will
    be cast as integers"""

    if not isinstance(var1, int):
        if allow_casting:
            var1 = int(var1)
        else:
            raise TypeError("Only integers are allowed")

    if not isinstance(var2, int):
        if allow_casting:
            var2 = int(var2)
        else:
            raise TypeError("Only integers are allowed")

    return var1 + var2
