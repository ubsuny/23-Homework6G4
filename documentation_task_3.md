# Details about Task 3

## Comparison of _numpy_ integration functions with that found in [Compphys](https://github.com/ubsuny/CompPhys/blob/main/Calculus/integrals.py)










This section explores and compares various numerical integration and root-finding methods in Python, specifically focusing on the integration functions provided by NumPy **(numpy.trapz(), numpy.simps(), numpy.adaptive_trapz()) and custom implementation functions (simpson(), trapezoid(), adaptive_trapezoid())**

**1. numpy.trapz()**
**Description:**

Calculates the definite integral of a function using the trapezoidal rule.

Usage:
```
import numpy as np
result = np.trapz(y, x)
```
**2. numpy.simps()**

**Description:**

Calculates the definite integral of a function using Simpson's rule.

**Usage:**
```
import numpy as np
result = np.simps(y, x)
```

**3. numpy.adaptive_trapz()**

**Description:**

An adaptive trapezoidal integration method using the NumPy library.

**Usage:**
```
import numpy as np
result = np.adaptive_trapz(func, a, b, ACC)
```
**4. simpson()
Description:**

Custom implementation of Simpson's rule for numerical integration.
**Usage:**
```
result = simpson(func, a, b, n)
```
**5. trapezoid()
Description:**

Custom implementation of the trapezoidal rule for numerical integration.
**Usage:**
```
result = trapezoid(func, a, b, n)
```
**6. adaptive_trapezoid()
Description:**

Custom implementation of an adaptive trapezoidal integration method.
**Usage:**

```
result = adaptive_trapezoid(func, a, b, acc)
```

**Example usage of numpy.trapz()**
```
import numpy as np
result_trapz = np.trapz(y, x)
```

**Example usage of simpson()**
```
result_simpson = simpson(func, a, b, n)
```












### Comparison Considerations
**Ease of Use:**

1. NumPy functions are easy to use and provide a concise syntax for integration.

2. Custom functions offer flexibility but may require more setup.

**Performance:**

1. NumPy functions are optimized and typically perform well.

2. Custom functions' performance may vary depending on the implementation.

**Adaptability:**

1. NumPy functions are general-purpose and work well for standard use cases.

2. Custom functions allow for specific adaptations to meet project requirements.

**Accuracy:**

1. NumPy functions are reliable and widely used in scientific computing.

2. Custom functions may require careful tuning for optimal accuracy.











## Addding missing docstrings in _calculus.py_
This part outlines the addition of missing docstrings to functions in the `calculus.py` file within the [Compphys](https://github.com/ubsuny/CompPhys/blob/main/Calculus/integrals.py) repository. The docstrings provide essential information about the purpose and usage of each function.

## calculus.py Functions

### `simpson(f, a, b, n)`

Approximates the definite integral of a given function using the composite Simpson's rule.

**Parameters:**
- `f`: Callable function representing the integrand.
- `a`: Lower bound of the integration interval.
- `b`: Upper bound of the integration interval.
- `n`: Number of subintervals.

**Returns:**
- Approximation of the definite integral.
  
**Example:**
```python
import numpy as np
from calculus import simpson

# Define a sample function for testing
def f(x):
    return x**2

# Integration bounds and number of subintervals
a = 0
b = 1
n = 100

# Perform the integration using Simpson's rule
result = simpson(f, a, b, n)
print(result)
```

## Github Actions for linting
n this repository, we use GitHub Actions to automate the linting process for Python code. This ensures that your code adheres to a consistent style and follows best practices. The linting workflow is triggered on every push to the repository.

Workflow Configuration
The linting workflow is defined in the .github/workflows/lint.yml file. This file tells GitHub Actions what to do when the specified event occurs, in this case, a push to the repository.

**Initial Result:**

<img width="550" alt="image" src="https://github.com/Mosaddeq107/23-Homework6G4/blob/main/Screenshot%202023-11-22%20at%2012.26.55%20PM.png">

**Result after making corrections:**

<img width="550" alt="image" src="https://github.com/Mosaddeq107/23-Homework6G4/blob/main/Screenshot%202023-11-22%20at%2012.30.03%20PM.png">

**Usage**
1. Ensure that you have a .github/workflows/lint.yml file in your repository with the provided configuration.

2. Make any necessary customizations based on your project structure and preferences.

3. On every push to the specified branch, GitHub Actions will automatically run the linting workflow and provide feedback on the code quality.

4. This setup helps maintain a consistent code style and catches potential issues early in the development process.

## Unit Testing:
We imported all the function from the **tests.py** and ran those unit tests function from **calculus.py** file from the main repository. 
The unit testing github action is below:
```
name: Unit testing with pytest

on: [push] # when should we run this action

jobs: # what should we do when it is run
  build:
    runs-on: ubuntu-latest # platform it runs on
    steps:
    - uses: actions/checkout@v4 # checkout your code
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10' # specify python version
    - name: Install dependencies # which libraries do we need for testing
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt # they should be listed in this file
    - name: Test with pytest
      run: |
        pip install pytest
        pytest tests.py
```
**Output**

<img width="550" alt="image" src="https://github.com/Mosaddeq107/23-Homework6G4/blob/main/Screenshot%202023-11-22%20at%203.06.08%20PM.png">

# Bibliography:
1. [Wikipedia](https://www.wikipedia.org/)
2. [Numpy Org](https://numpy.org/)
3. [OpenAI](https://chat.openai.com/)
4. [Compphys](https://github.com/ubsuny/CompPhys)
