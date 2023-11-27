import numpy as np
from calculus import simpon, trapezoid, adaptive_trapezoid
import scipy.integrate

# Test functions with safe handling for singularities near x = 0.

# This function calculates exp(-1/x). It avoids issues when x is very close to 0.
def exp(x):
    # Clip x to a minimum of 1e-10 to avoid division by zero or extremely small numbers.
    safe_x = np.clip(x, 1e-10, np.inf)
    # Calculate exp(-1/x) normally when x is not zero; return 0 when x is zero.
    return np.where(x != 0, np.exp(-1/safe_x), 0)

# This function calculates cos(1/x), similarly handling issues at x = 0.
def cos(x):
    # Again, clip x to avoid division by extremely small numbers.
    safe_x = np.clip(x, 1e-10, np.inf)
    # Calculate cos(1/x) normally when x is not zero; return 1 (cos(∞)) when x is zero.
    return np.where(x != 0, np.cos(1/safe_x), 1)

# A simple cubic function for testing: x^3 + a constant.
def cubic(x, constant=1/2):
    # No special handling needed here, as there are no singularities in this function.
    return x**3 + constant

# Parameters for numerical integration
group_number = 2
epsilon = 1e-10  # A small number used to avoid dividing by zero in the functions.
# Defining intervals over which to integrate. The first two avoid starting at 0.
intervals = [(epsilon, 20*group_number), (epsilon, np.pi*group_number), (-1, 1)]
n = 1000  # Number of subintervals for non-adaptive methods (Simpson's and Trapezoidal)
accuracy = 1e-3  # Desired accuracy for the adaptive method

# Function to calculate the number of correct digits in the numerical result
def correct_digits(actual, reference):
    # Compute the absolute difference between the actual result and reference
    error = np.abs(actual - reference)
    # Check if the reference value is non-zero
    if reference != 0:
        # Calculate relative error (error as a fraction of the reference value)
        relative_error = error / np.abs(reference)
        # If relative error is zero, we have perfect accuracy
        if relative_error == 0:
            return np.inf  # Indicate perfect accuracy with infinity
        # Calculate the number of correct digits using the base-10 logarithm of the relative error
        return -np.log10(relative_error)
    else:
        # If reference value is zero, check if the error is also zero
        if error == 0:
            return np.inf  # Perfect accuracy
        # For non-zero error when reference is zero, calculate digits based on absolute error
        return -np.log10(error)

# Assessing accuracy and efficiency of numerical integration methods
for func in [exp, cos, lambda x: cubic(x, 1/group_number)]:
    for a, b in intervals:
        # Compute a reference value using scipy's quad method for accurate comparison
        reference_value, _ = scipy.integrate.quad(func, a, b)

        # Simpson's Rule: A numerical method for estimating integrals
        simpson_integral = simpson(func, a, b, n)
        # Calculate the absolute error compared to the reference value
        simpson_error = np.abs(simpson_integral - reference_value)
        # Estimate the number of correct digits in the Simpson's rule result
        simpson_digits = correct_digits(simpson_integral, reference_value)

        # Trapezoidal Rule: Another method for estimating integrals
        trapezoid_integral = trapezoid(func, a, b, n)
        # Calculate the absolute error for the Trapezoidal rule
        trapezoid_error = np.abs(trapezoid_integral - reference_value)
        # Estimate the number of correct digits in the Trapezoidal rule result
        trapezoid_digits = correct_digits(trapezoid_integral, reference_value)

        # Adaptive Trapezoidal Rule: Adjusts its method based on desired accuracy
        adaptive_integral, adaptive_evaluations = adaptive_trapezoid(func, a, b, accuracy)
        # Calculate the absolute error for the Adaptive Trapezoidal rule
        adaptive_error = np.abs(adaptive_integral - reference_value)
        # Estimate the number of correct digits for the Adaptive Trapezoidal rule
        adaptive_digits = correct_digits(adaptive_integral, reference_value)

        # Print results for comparison
        print(f"Function: {func.__name__}, Interval: [{a}, {b}]")
        print(f"Reference Value: {reference_value}")
        print(f"Simpson's Rule: Integral = {simpson_integral}, Error = {simpson_error}, Correct Digits = {simpson_digits}")
        print(f"Trapezoidal Rule: Integral = {trapezoid_integral}, Error = {trapezoid_error}, Correct Digits = {trapezoid_digits}")
        print(f"Adaptive Trapezoidal Rule: Integral = {adaptive_integral}, Error = {adaptive_error}, Correct Digits = {adaptive_digits}, Evaluations = {adaptive_evaluations}")
        print("-" * 50)
