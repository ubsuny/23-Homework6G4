"""
This is a unit testing file for the integral and root finding.
"""
import sys
import unittest
from io import StringIO
from calculus import simpson, trapezoid, adaptive_trapezoid, root_print_header, root_simple, root_secant, root_bisection, root_tangent


class TestCalculusFunctions(unittest.TestCase):
    """
    Test various functions from the calculus module.
    """

    def test_simpson(self):
        """Test the simpson function with a known integral."""
        # Define the integrand function
        def f(x):
            return x**2

        # Initial guesses and expected outcome
        a = 0
        b = 2
        n = 100
        expected_integral = 8/3

        # Call the simpson function
        result = simpson(f, a, b, n)

        # Check if the result is close to the expected integral
        self.assertAlmostEqual(result, expected_integral, places=5)

    def test_trapezoid(self):
        """Test the trapezoid function with a known integral."""

        # Define the integrand function
        def f(x):
            return x**3

        # Initial guesses and expected outcome
        a = 0
        b = 2
        n = 500
        expected_integral = 4

        # Call the trapezoid function
        result = trapezoid(f, a, b, n)

        # Check if the result is close to the expected integral
        self.assertAlmostEqual(result, expected_integral, places=3)

    def test_adaptive_trapezoid(self):
        """Test the adaptive_trapezoid function with a known integral."""
        # Define the integrand function
        def f(x):
            return x**2

        # Initial guesses and expected outcome
        a = 1
        b = 2
        expected_integral = 7/3

        # Call the adaptive_trapezoid function
        result = adaptive_trapezoid(f, a, b, acc=1e-7)

        # Check if the result is close to the expected integral
        self.assertAlmostEqual(result, expected_integral, places=5)

    def test_root_simple(self):
        """Test the root_simple function with a known root."""
        # Define the function
        def f(x):
            return x**2 - 4

        # Initial guesses and expected outcome
        x = -3.0
        dx = 0.1
        expected_root = -2.0

        # Call the root_simple function
        result, _ = root_simple(f, x, dx, accuracy=1e-6)

        # Check if the result is close to the expected root
        self.assertAlmostEqual(result, expected_root, places=5)

    def test_root_bisection(self):
        """Test the root_bisection function with a known root."""
        # Define the function
        def f(x):
            return x**2 - 4

        # Initial guesses and expected outcome
        x1 = 1
        x2 = 4
        expected_root = 2.0

        # Call the root_bisection function
        result, _ = root_bisection(f, x1, x2, accuracy=1e-6)

        # Check if the result is close to the expected root
        self.assertAlmostEqual(result, expected_root, places=5)

    def test_root_secant(self):
        """Test the root_secant function with a known root."""
        # Define the function
        def f(x):
            return x**2 - 4

        # Initial guesses and expected outcome
        x0 = 0.5
        x1 = 3.5
        expected_root = 2.0

        # Call the root_secant function
        result, _ = root_secant(f, x0, x1, accuracy=1e-6)

        # Check if the result is close to the expected root
        self.assertAlmostEqual(result, expected_root, places=5)

    def test_root_tangent(self):
        """Test the root_tangent function with a known root."""
        # Define the function and its derivative
        def f(x):
            return x**2 - 4

        def fp(x):
            return 2*x

        # Initial guesses and expected outcome
        x0 = -1.5
        expected_root = -2.0

        # Call the root_tangent function
        result = root_tangent(f, fp, x0, accuracy=1e-6)

        # Check if the result is close to the expected root
        self.assertAlmostEqual(result, expected_root, delta=1e-6)

    def test_root_print_header_output(self):
        """Test if root_print_header produces the correct output."""
        # Redirect stdout to capture the printed output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the root_print_header function
        algorithm = "Test Algorithm"
        accuracy = 1e-6
        root_print_header(algorithm, accuracy)

        # Get the captured output
        result = captured_output.getvalue()

        # Reset redirect.
        sys.stdout = sys.__stdout__

        # Define the expected output
        expected_output = (
            "\n ROOT FINDING using Test Algorithm"
            "\n Requested accuracy = 1e-06"
            "\n Step     Guess For Root          Step Size      "
            "     Function Value"
            "\n ----  --------------------  --------------------"
            "  --------------------\n"
        )

        # Check if the result matches the expected output
        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
