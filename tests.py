""" 
This is a unit testing file for the integral and root finding.
"""
import numpy as np
import pytest
from calculus import simpson, trapezoid, adaptive_trapezoid

def test_simpson_known_integral(self):
        """Test the simpson function with a known integral."""
        # Define the integrand function
        def f(x):
            return x**2

        # Integration limits
        a = 0
        b = 1

        # Number of subintervals (even for Simpson's rule)
        n = 100

        # Expected result (known integral of x^2 from 0 to 1)
        expected_integral = 1/3

        # Call the simpson function
        result = simpson(f, a, b, n)

        # Check if the result is close to the expected integral
        self.assertAlmostEqual(result, expected_integral, places=5)

    def test_trapezoid_known_integral(self):
        """Test the trapezoid function with a known integral."""

        # Define the integrand function
        def f(x):
            return x**3

        # Integration limits
        a = 0
        b = 1

        # Number of subintervals
        n = 100

        # Expected result (known integral of x^3 from 0 to 1)
        expected_integral = 1/4

        # Call the trapezoid function
        result = trapezoid(f, a, b, n)

        # Check if the result is close to the expected integral
        self.assertAlmostEqual(result, expected_integral, places=3)   # Adjust places as needed

    def test_adaptive_trapezoid_known_integral(self):
        """Test the adaptive_trapezoid function with a known integral."""
        # Define the integrand function
        def f(x):
            return x**2

        # Integration limits
        a = 0
        b = 1

        # Expected result (known integral of x^2 from 0 to 1)
        expected_integral = 1/3

        # Call the adaptive_trapezoid function
        result = adaptive_trapezoid(f, a, b, acc=1e-6)

        # Check if the result is close to the expected integral
        self.assertAlmostEqual(result, expected_integral, places=5)

