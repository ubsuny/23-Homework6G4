# Summary of task 1
I used three different methods simpsons, trapezoid and adaptive trapezoid to find the integral values of three different functions given. These three different methods using diffrent techniques
to evaluate the integral between the intervals. Simpsons rule  fits a parabolic segment over every two consecutive intervals and integrates the parabola to approximate the area. 
The Trapezoidal rule approximates the area under the curve by dividing the region into trapezoids and summing up their areas. Adaptive trapezoidal rule recursively apply the trapezoidal rule to subintervals until a specified accuracy is achieved.

Using the module file calculas.py from (https://github.com/ubsuny/CompPhys/blob/main/Calculus/integrals.py) I estimate the integral value and plots of three different (exponential, cosine 
and cubic function) The boundary given [0, 10.group number] and [0, pi.group number] encounters the zero error while integrating as the function is defined as exp(-1/x) and cos(1/x). Thus to 
avoid the zero error, I consider infinitesimal value close to zero and modified the code so that the integral value doesnot change.
``` python
def f(x):
  safe_x = np.clip(x, 1e-6, np.inf)
  return np.where(x != 0, np.cos(1/safe_x), 0)
```
Further to compare the accuracy I use scipy library and find the integral value. On importing quad from scipy.integrate library the exact value of integration for each function is estimated.
``` python
from scipy.integrate import quad
result, error = quad(f, a, b)
print(f"The result of the integration is: {result}")
```
The result of integration obtained by using scipy is compared to that of different method (simpsons, trapezoid and adaptive trapezoid) to estimate the accuracy of values obtained up to how 
much digits.
``` python
#Use the simpson function to calculate the integral
result_simpson = simpson(f, a, b, n)

#Use the trapezoid function to calculate the integral
result_trapezoid = trapezoid(f, a, b, n)

#Perform adaptive trapezoidal integration
result_adaptive_trapezoid = adaptive_trapezoid(f, a, b, desired_accuracy, output=False)

#Calculate accuracies
accuracy_simpson = -math.log10(np.abs((result_simpson - result) / result))
accuracy_trapezoid = -math.log10(np.abs((result_trapezoid - result) / result))
accuracy_adaptive_trapezoid = -math.log10(np.abs((result_adaptive_trapezoid - result) / result))

print(f"Accuracy of Simpson's rule: {accuracy_simpson} digits")
print(f"Accuracy of trapezoid rule: {accuracy_trapezoid} digits")
print(f"Accuracy of adaptive trapezoid rule: {accuracy_adaptive_trapezoid} digits")

```
Thus on comparing the accuracies I found the accuracy values for cos(1/x) as:

- The result of the integration is: 11.035262811666506
- Accuracy of Simpson's rule: 1.649983453420165 digits
 - Accuracy of trapezoid rule: 1.4299534692265436 digits
 - Accuracy of adaptive trapezoid rule: 3.9973860670879406 digits
   
The estimation of interagration value and comparision of accuracy is carried out likewise for other two functions also.

Further to calculate the efficiencies the function is defined such that in addition to inegral value it gives the iteration steps needed to reach the acciracy value of 1e-3.
The code used an approach where the number of subintervals is dramatically adjusted to improve the accuracy of integral untill the desired accuracy is achieved. The function calls and returns
the improved integral value and the number of iterations it took to reach the desired accuracy value.
```python
def compute_simpson_integral(n):
        h = (b - a) / n
        i = np.arange(0, n)
        s = f(a) + f(b) + 4 * np.sum(f(a + i[1::2] * h)) + 2 * np.sum(f(a + i[2:-1:2] * h))
        return s * h / 3

    old_integral = compute_simpson_integral(n)
    iterations = 1
    while True:
        n *= 2
        new_integral = compute_simpson_integral(n)
        if np.abs(new_integral - old_integral) < accuracy:
            return new_integral, iterations
        old_integral = new_integral
        iterations += 1
```
The method employed is similar to both simpsons and trapezoid  with iteration initialized at 1 for adaptive trapezoid method, iteration is initialized at zero.
``` python
def adaptive_trapezoid(f, a, b, accuracy):
  """
    Approximate the definite integral of a given function using Adaptive trapezoid's rule.

    Parameters:
    - f (function): The integrand function.
    - a (float): The lower limit of integration.
    - b (float): The upper limit of integration.
    - n (int): The initial number of subintervals for adaptive trapezoid rule.
    - accuracy (float): The desired accuracy for the approximation.

    Returns:
    -  Approximate integral value and the number of iterations
      required to achieve specified accuracy.
    """
  old_s = np.inf
  h = b - a
  n = 1
  s = (f(a) + f(b)) * 0.5
  iterations = 0  # Initialize iteration counter

  while abs(h * (old_s - s * 0.5)) > accuracy:
        iterations += 1  # Increment the iteration counter
        old_s = s
        for i in np.arange(n):
            s += f(a + (i + 0.5) * h)
        n *= 2
        h *= 0.5

  return h * s, iterations  # Return the integral and the number of iterations
```
Code implemented to find the iteration steps for each method with imported module file iteration.py.
   
  ```python
import math
import numpy as np
import matplotlib.pyplot as plt
from math import pi
from scipy.integrate import quad
# Import the simpson function from calculus.py (assuming it's in the same directory)
from iteration import *

"""
 Numerical integration techniques for the function f(x) = cos(1/x) over a given interval.
Functions:
- f(x): The function to be integrated,with special handling for x=0 to avoid numerical issues.
- simpson(f, a, b, n): Implementation of Simpson's rule for numerical integration.
- trapezoid(f, a, b, n): Implementation of the trapezoidal rule for numerical integration.
- adaptive_trapezoid(f, a, b, desired_accuracy, output): Implementation of adaptive trapezoidal integration.

Variables:
- a: Lower bound of the integration interval.
- b: Upper bound of the integration interval.
- n: Number of subintervals for Simpson's and trapezoidal rule.
- desired_accuracy: Desired accuracy for the adaptive trapezoidal integration.
- simpson_integral, trapezoid_integral, adaptive_integral: Results of numerical integration.
"""
# Avoid division by zero
# Function to calculate cos(1/x) with handling for x near 0
def f(x):
    safe_x = np.clip(x, 1e-10, np.inf)
    return np.where(x != 0, np.cos(1/safe_x), 0)

 # Define the integration bounds
a = 1e-6
b = 4 * np.pi
accuracy = 1e-3
#result, error = quad(f, a, b)

# Define the number of subintervals
n = 20
simpson_integral, simpson_iterations = simpson(f, a, b, n, accuracy)
trapezoid_integral, trapezoid_iterations = trapezoid(f, a, b, n, accuracy)
adaptive_integral, adaptive_evaluations = adaptive_trapezoid(f, a, b, accuracy)

print(f"Simpson: Integral = {simpson_integral}, Func = cos(1/x), Iterations = {simpson_iterations}")
print(f"Trapezoidal: Integral = {trapezoid_integral}, Func = cos(1/x), Iterations = {trapezoid_iterations}")
print(f"Adaptive Trapezoidal : Integral = {adaptive_integral}, Func = cos(1/x), Evaluations = {adaptive_evaluations}")
```
The output for the code implemented:
   

- Simpson: Integral = 11.035108805732696, Func = cos(1/x), Iterations = 10
- Trapezoidal: Integral = 11.035231063180158, Func = cos(1/x), Iterations = 10
- Adaptive Trapezoidal : Integral = 11.034152623449767, Func = cos(1/x), Evaluations = 13

Outputs and plots of all functions are included in the task 1 folder of group 6 homework repository. 

## References

https://github.com/ubsuny/CompPhys/blob/main/Calculus/
