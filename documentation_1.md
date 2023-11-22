# Summary of task 1
I used three different methods simpsons, trapezoid and adaptive trapezoid to find the integral values of three different functions given. These three different methods using diffrent techniques
to evaluate the integral between the intervals. Simpsons rule  fits a parabolic segment over every two consecutive intervals and integrates the parabola to approximate the area. 
The Trapezoidal rule approximates the area under the curve by dividing the region into trapezoids and summing up their areas. Adaptive trapezoidal rule recursively apply the trapezoidal rule to subintervals until a specified accuracy is achieved.

Using the module file calculas.py from (https://github.com/ubsuny/CompPhys/blob/main/Calculus/integrals.py) I estimate the integral value and plots of three different (exponential, cosine 
and cubic function) The boundary given [0, 10.group number] and [0, pi.group number] encounters the zero year while integrating as the function is defined as exp(-1/x) and cos(1/x). Thus to 
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
The method employed is similar to both simpsons and trapezoid with initial iteration starting from 1.

   
