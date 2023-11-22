""" 
This is a unit testing file for the integral and root finding
"""
import numpy as np
import pytest
from calculus import simpson, trapezoid, adaptive_trapezoid

def test_simpson():
    # Define a sample function for testing
    def f(x):
        return x**2

    # Initial guess for integration bounds and number of subintervals
    a = 0
    b = 1
    n = 100

    # Calculate the expected result
    expected_result = 1/3

    # Perform the integration using simpson and assert the result
    result = simpson(f, a, b, n)
    assert np.isclose(result, expected_result, rtol=1e-5)


def test_trapezoid():
    # Define a sample function for testing
    def f(x):
        return x**2

    # Initial guess for integration bounds and number of subintervals
    a = 0
    b = 1
    n = 100

    # Calculate the expected result
    expected_result = 1/3

    # Perform the integration using trapezoid and assert the result
    result = trapezoid(f, a, b, n)
    assert np.isclose(result, expected_result, rtol=1e-5)


def test_adaptive_trapezoid():
    # Define a sample function for testing
    def f(x):
        return x**2

    # Initial guess for integration bounds and accuracy
    a = 0
    b = 1
    acc = 1e-5

    # Calculate the expected result
    expected_result = 1/3

    # Perform the integration using adaptive_trapezoid and assert the result
    result = adaptive_trapezoid(f, a, b, acc)
    assert np.isclose(result, expected_result, rtol=1e-5)
