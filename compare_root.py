import rootfinding_calculas as calc
import numpy as np

def compare_steps(f_input):
    """
    Compare the number of steps to find the roots using root_simple and root_secant algorithms.

    Parameters:
    - f_input: function
        The function for which roots are to be found.

    Returns:
    tuple: (steps_simple, steps_secant)
        The number of steps taken by root_simple and root_secant algorithms.
    """
    start = (np.random.rand() - 0.5) * 4
    steps_simple = len(calc.root_simple(f_input, start, 0.01, root_debug=True, max_steps=10000)[1])
    steps_secant = len(calc.root_secant(f_input, start, np.random.rand() * start, root_debug=True, max_steps=10000)[1])
    return steps_simple, steps_secant

def compare_accuracy(f_input, true_root):
    """
    Compare the accuracy of roots found using root_simple and root_secant algorithms.

    Parameters:
    - f_input: function
        The function for which roots are to be found.
    - true_root: float
        The true root of the function.

    Returns:
    tuple: (acc_simple, acc_secant)
        The accuracy of roots found by root_simple and root_secant algorithms.
    """
    start = (np.random.rand() - 0.5) * 4
    rt_simple = calc.root_simple(f_input, start, 0.1, max_steps=10000)[0]
    rt_secant = calc.root_secant(f_input, start, np.random.rand() * start, max_steps=10000)[0]
    acc_simple = abs(rt_simple - true_root)
    acc_secant = abs(rt_secant - true_root)
    return acc_simple, acc_secant

def average_steps(f_input, trials):
    """
    Calculate the average number of steps for root_simple and root_secant algorithms.

    Parameters:
    - f_input: function
        The function for which roots are to be found.
    - trials: int
        The number of trials for averaging.

    Returns:
    tuple: (avg_simple, avg_secant)
        The average number of steps taken by root_simple and root_secant algorithms.
    """
    simple_array, secant_array = [], []
    for _ in range(trials):
        simple, secant = compare_steps(f_input)
        simple_array.append(simple)
        secant_array.append(secant)
    avg_simple, avg_secant = np.average(simple_array), np.average(secant_array)
    return avg_simple, avg_secant

def average_accuracy(f_input, true_root, trials):
    """
    Calculate the average accuracy of roots for root_simple and root_secant algorithms.

    Parameters:
    - f_input: function
        The function for which roots are to be found.
    - true_root: float
        The true root of the function.
    - trials: int
        The number of trials for averaging.

    Returns:
    tuple: (avg_simple, avg_secant)
        The average accuracy of roots found by root_simple and root_secant algorithms.
    """
    simple_array, secant_array = [], []
    for _ in range(trials):
        simple, secant = compare_accuracy(f_input, true_root)
        simple_array.append(simple)
        secant_array.append(secant)
    avg_simple, avg_secant = np.average(simple_array), np.average(secant_array)
    return avg_simple, avg_secant

print("For Tangent:\n")

simp_avg, sec_avg = average_steps(np.tan, 1000)
print(f"For the two algorithms with the same starting guess, the simple root finder takes an average of {simp_avg} steps, while the secant takes {sec_avg} steps.\n")

simp_avg, sec_avg = average_accuracy(np.tan, 0, 1000)
print(f"For the two algorithms with the same starting guess and 50 max steps, the simple root finder is within {simp_avg} of the true root, while the secant is within {sec_avg} on average, i.e., the secant root error is {100 * sec_avg / simp_avg}% of the simple root error.\n")

# Uncomment the following section if needed
# print("For Hyperbolic Tangent:\n")
# simp_avg, sec_avg = average_steps(np.tanh, 1000)
# print(f"For the two algorithms with the same starting guess, the simple root finder takes an average of {simp_avg} steps, while the secant takes {sec_avg} steps.\n")
# simp_avg, sec_avg = average_accuracy(np.tanh, 0, 1000)
# print(f"For the two algorithms with the same starting guess and 50 max steps, the simple root finder is within {simp_avg} of the true root, while the secant is within {sec_avg} on average, i.e., the secant root error is {100 * sec_avg / simp_avg}% of the simple root error.")
