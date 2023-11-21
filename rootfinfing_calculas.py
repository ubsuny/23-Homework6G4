import math
import sys
import cmath
import numpy as np


def root_print_header(algorithm, accuracy):
    """Prints the header for the root-finding algorithm.

    Parameters:
    - algorithm (str): The name of the root-finding algorithm.
    - accuracy (float): The specified accuracy for the root.
    """
    sys.stdout.write("\n ROOT FINDING using " + algorithm +
                     "\n Requested accuracy = " +repr(accuracy) +
                     "\n Step     Guess For Root          Step Size      " +
                     "     Function Value" +
                     "\n ----  --------------------  --------------------" +
                     "  --------------------" + "\n")


