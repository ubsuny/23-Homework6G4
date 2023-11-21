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


def root_print_step(step, x, dx, f_of_x):
    """Prints the details of each iteration step in the root-finding algorithm.

    Parameters:
    - step (int): The current iteration step.
    - x (float): The guess for the root.
    - dx (float): The step size.
    - f_of_x (float): The function value at the current guess.
    """
    sys.stdout.write(repr(step).rjust(5))
    for val in [x, dx, f_of_x]:
        sys.stdout.write("  " + repr(val).ljust(20))
    sys.stdout.write("\n")

def root_max_steps(algorithm, max_steps):
    """Raises an exception when the maximum number of steps is exceeded.

    Parameters:
    - algorithm (str): The name of the root-finding algorithm.
    - max_steps (int): The maximum number of allowed steps.
    """
    raise Exception(" " + algorithm + ": maximum number of steps " +
                    repr(max_steps) + " exceeded\n")



