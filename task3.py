import math

def fibonacci_recursive(n, depth=0, max_depth=20):
    """
    Calculate the n-th Fibonacci number using recursion with depth limitation.
    
    :param n: The position of the Fibonacci number to calculate.
    :param depth: The current depth of recursion.
    :param max_depth: The maximum allowed depth for recursion.
    :return: The n-th Fibonacci number or an approximate value if depth limit is reached.
    """
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    # Check if the recursion depth limit is reached
    if depth >= max_depth:
        print(f"Depth limit reached at n={n}. Returning approximate value.")
        phi = (1 + math.sqrt(5)) / 2  # Golden ratio
        return int(round((phi ** n) / math.sqrt(5)))

    # Recursive calculation with depth tracking
    return fibonacci_recursive(n - 1, depth + 1, max_depth) + fibonacci_recursive(n - 2, depth + 1, max_depth)

# Example usage:
n = 35
max_depth = 20
result = fibonacci_recursive(n, max_depth=max_depth)
print(f"The {n}-th Fibonacci number is: {result}")
