"""
calculus.py - A module for numerical integration and root-finding algorithms.

This module provides functions for numerical integration using Simpson's rule,
the trapezoidal rule, and the adaptive trapezoidal method. It also includes
root-finding algorithms such as simple root, bisection, secant, and tangent methods.
"""

# import math
import sys
# import cmath
import numpy as np


def simpson(f, a, b, n):
    """Approximates the definite integral of f from a to b by
    the composite Simpson's rule, using n subintervals.
    From http://en.wikipedia.org/wiki/Simpson's_rule
    """
    h = (b - a) / n
    i = np.arange(0, n)

    s = f(a) + f(b)
    s += 4 * np.sum(f(a + i[1::2] * h))
    s += 2 * np.sum(f(a + i[2:-1:2] * h))

    return s * h / 3


def trapezoid(f, a, b, n):
    """Approximates the definite integral of f from a to b by
    the composite trapezoidal rule, using n subintervals.
    From http://en.wikipedia.org/wiki/Trapezoidal_rule
    """
    h = (b - a) / n
    s = f(a) + f(b)
    i = np.arange(0, n)
    s += 2 * np.sum(f(a + i[1:] * h))
    return s * h / 2


def adaptive_trapezoid(f, a, b, acc, output=False):
    """
    Uses the adaptive trapezoidal method to compute the definite integral
    of f from a to b to desired accuracy acc.
    """
    old_s = np.inf
    h = b - a
    n = 1
    s = (f(a) + f(b)) * 0.5
    if output:
        print("N = " + str(n + 1) + ",  Integral = " + str(h * s))
    while abs(h * (old_s - s * 0.5)) > acc:
        old_s = s
        for i in np.arange(n):
            s += f(a + (i + 0.5) * h)
        n *= 2.0
        h *= 0.5
        if output:
            print("N = " + str(n) + ",  Integral = " + str(h * s))
    return h * s


def root_print_header(algorithm, accuracy):
    """
    Display the header for root-finding iterations.

    This function prints a formatted header to the standard output, providing
    information about the root-finding algorithm being used, the requested accuracy,
    and column headers for the iterative steps.

    Parameters:
    - algorithm (str): The name of the root-finding algorithm being used.
    - accuracy (float): The requested accuracy for the root-finding process.
    """
    sys.stdout.write(
        "\n ROOT FINDING using "
        + algorithm
        + "\n Requested accuracy = "
        + repr(accuracy)
        + "\n Step     Guess For Root          Step Size      "
        + "     Function Value"
        + "\n ----  --------------------  --------------------"
        + "  --------------------"
        + "\n"
    )


def root_print_step(step, x, dx, f_of_x):
    """
    Display information about a step in the root-finding process.

    This function prints the details of a single step in the root-finding process,
    including the step number, the current guess for the root, the step size, and
    the corresponding function value.

    Parameters:
    - step (int): The step number in the root-finding iteration.
    - x (float): The current guess for the root.
    - dx (float): The step size taken in the iteration.
    - f_of_x (float): The function value at the current guess.
    """
    sys.stdout.write(repr(step).rjust(5))
    for val in [x, dx, f_of_x]:
        sys.stdout.write("  " + repr(val).ljust(20))
    sys.stdout.write("\n")


def root_max_steps(algorithm, max_steps):
    """
    Raise an exception indicating that the maximum number of steps has been exceeded.

    This function raises an exception when the maximum number of steps allowed in a
    root-finding algorithm has been exceeded. It provides information about the
    algorithm name and the specified maximum number of steps.

    Parameters:
    - algorithm (str): The name of the root-finding algorithm.
    - max_steps (int): The maximum number of steps allowed.
    """
    raise Exception(
        " " + algorithm + ": maximum number of steps " + repr(max_steps) + " exceeded\n"
    )


def root_simple(f, x, dx, accuracy=1.0e-6, max_steps=1000, root_debug=False):
    """Return root of f(x) given guess x and step dx with specified accuracy.
    Step must be in direction of root: dx must have same sign as (root - x).
    """
    f0 = f(x)
    fx = f0
    step = 0
    iterations = []
    if root_debug:
        iterations.append([x, f0])
    while abs(dx) > abs(accuracy) and f0 != 0.0:
        x += dx
        fx = f(x)
        if f0 * fx < 0.0:  # stepped past root
            x -= dx  # step back
            dx /= 2.0  # use smaller step
        step += 1
        if step > max_steps:
            root_max_steps("root_simple", max_steps)
        if root_debug:
            iterations.append([x, fx])
    return x, np.array(iterations)


def root_bisection(f, x1, x2, accuracy=1.0e-6, max_steps=1000, root_debug=False):
    """Return root of f(x) in bracketed by x1, x2 with specified accuracy.
    Assumes that f(x) changes sign once in the bracketed interval.
    Uses bisection root-finding algorithm.
    """
    iterations = []
    f1 = f(x1)
    f2 = f(x2)
    if f1 * f2 > 0.0:
        raise Exception("f(x1) * f(x2) > 0.0")
    x_mid = (x1 + x2) / 2.0
    f_mid = f(x_mid)
    dx = x2 - x1
    step = 0
    if root_debug:
        iterations.append([x_mid, f_mid])
    while abs(dx) > accuracy:
        if f_mid == 0.0:
            dx = 0.0
        else:
            if f1 * f_mid > 0:
                x1 = x_mid
                f1 = f_mid
            else:
                x2 = x_mid
                f2 = f_mid
            x_mid = (x1 + x2) / 2.0
            f_mid = f(x_mid)
            dx = x2 - x1
        step += 1
        if step > max_steps:
            warning = "Too many steps (" + repr(step) + ") in root_bisection"
            raise Exception(warning)
        if root_debug:
            iterations.append([x_mid, f_mid])
    return x_mid, np.array(iterations)


def root_secant(f, x0, x1, accuracy=1.0e-6, max_steps=20, root_debug=False):
    """Return the root of the function f(x) given initial guesses x0 and x1
    with specified accuracy. Uses the secant root-finding algorithm.

    Parameters:
    - f: Callable function representing the equation f(x) for which the root is sought.
    - x0: Initial guess for the root.
    - x1: Another initial guess for the root.
    - accuracy: Desired accuracy of the root. The algorithm stops when the change in x is smaller than this value.
    - max_steps: Maximum number of iterations allowed.
    - root_debug: If True, store and return the iteration history for debugging purposes.

    Returns:
    - The root of the function f(x).

    Raises:
    - Exception: If the secant line becomes horizontal (f(x0) = f(x1)) during the iteration.

    Notes:
    - If f(x0) or f(x1) is already close to zero, x0 or x1 is returned as the root.
    - If the iteration exceeds the maximum number of steps, an exception is raised.
    """
    iterations = []
    f0 = f(x0)
    dx = x1 - x0
    step = 0
    if root_debug:
        iterations.append([x0, f0])
    if f0 == 0:
        return x0
    while abs(dx) > abs(accuracy):
        f1 = f(x1)
        if f1 == 0:
            return x1
        if f1 == f0:
            raise Exception("Secant horizontal f(x0) = f(x1) algorithm fails")
        dx *= -f1 / (f1 - f0)
        x0 = x1
        f0 = f1
        x1 += dx
        step += 1
        if step > max_steps:
            root_max_steps("root_secant", max_steps)
        if root_debug:
            iterations.append([x1, f1])
    return x1, np.array(iterations)


def root_tangent(f, fp, x0, accuracy=1.0e-6, max_steps=20, root_debug=False):
    """
    Return the root of the function f(x) with its derivative fp(x) using
    the Newton-Raphson (tangent) root-finding algorithm.

    Parameters:
    - f: Callable function representing the equation f(x) for which the root is sought.
    - fp: Callable function representing the derivative of f(x) with respect to x.
    - x0: Initial guess for the root.
    - accuracy: Desired accuracy of the root. The algorithm stops when the change in x is smaller than this value.
    - max_steps: Maximum number of iterations allowed.
    - root_debug: If True, store and return the iteration history for debugging purposes.

    Returns:
    - The root of the function f(x).

    Raises:
    - Exception: If the derivative fp(x) becomes zero during the iteration.

    Notes:
    - If f(x0) is already close to zero, x0 is returned as the root.
    - If the iteration exceeds the maximum number of steps, an exception is raised.
    """
    iterations = []
    f0 = f(x0)
    fp0 = fp(x0)
    if fp0 == 0.0:
        raise Exception(" root_tangent df/dx = 0 algorithm fails")
    dx = -f0 / fp0
    step = 0
    if root_debug:
        iterations.append([x0, f0])
    if f0 == 0.0:
        return x0
    while True:
        fp0 = fp(x0)
        if fp0 == 0.0:
            raise Exception(" root_tangent df/dx = 0 algorithm fails")
        dx = -f0 / fp0
        x0 += dx
        f0 = f(x0)
        if abs(dx) <= accuracy or f0 == 0.0:
            return x0
        step += 1
        if step > max_steps:
            root_max_steps("root_tangent", max_steps)
        if root_debug:
            iterations.append([x0, f0])
    return x0
