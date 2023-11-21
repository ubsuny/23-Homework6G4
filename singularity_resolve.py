from calculus import simpson, trapeziod, adaptive_trapezoid
import numpy as np
import matplotlib.pyplot as plt

# def exp_minus_1_over_x(x):
#     # To handle the singularity at x = 0
#     return np.where(x != 0, np.exp(-1/x), 0)

# def cos_1_over_x(x):
#     # To handle the singularity at x = 0
#     return np.where(x !=0, np.cos(1/x),0)

# However, there is still a RuntimeWarning that encountred  due to the behavior
# of the functions exp and cos near zero. These functions have singularities or
# behave erratically as x approaches zero. We can resolve this issue by modifying
# functions:
def exp_minus_1_over_x(x):
    # Using np.exp safely with np.clip to avoid overflow
    safe_x = np.clip(x, 1e-10, np.inf) #np.clip is used to limit the values of x
                                      # to a range that avoids division by zero
                                      # and overflow issues. It effectively replaces
                                      # very small values (close to zero) with a small
                                      # but non-zero number (1e-10 in this case).
    return np.where(x != 0, np.exp(-1/safe_x), 0)
    """
Computes the exponential of -1 divided by x, using numpy.exp and numpy.clip to avoid overflow.

Args:
  x (float): The number to be used in the exponential calculation.

Returns:
  float: The exponential of -1 divided by x, with safe clipping to avoid overflow.
"""

def cos_1_over_x(x):
    # Limiting the input to cos to avoid invalid values
    safe_x = np.clip(x, 1e-10, np.inf)
    return np.where(x != 0, np.cos(1/safe_x), 1)


def x_cubed_plus_constant(x, constant=1/2):
    return x**3 + constant
    """
Computes the cube of a number plus a specific constant.

Args:
  x (float): The number to be cubed.
  constant (float, optional): The constant to be added to the cubed number. Defaults to 1/2.

Returns:
  float: The cube of the number plus the constant.
"""
