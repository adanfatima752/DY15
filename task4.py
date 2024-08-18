def adaptive_quadrature(func, a, b, tol=1e-6):
    """
    Integrate the given function func over the range [a, b] using adaptive quadrature.
    
    :param func: The function to be integrated.
    :param a: The start of the interval.
    :param b: The end of the interval.
    :param tol: The tolerance level for the integration accuracy.
    :return: The estimated integral value.
    """
    def quad_recursive(f, a, b, tol, whole):
        c = (a + b) / 2.0
        left = (f(a) + 4 * f(c) + f(b)) * (b - a) / 12.0
        right = (f(a) + 4 * f((a + c) / 2.0) + f(c)) * (c - a) / 6.0
        new_whole = left + right
        
        if abs(new_whole - whole) <= tol:
            return new_whole
        else:
            return (quad_recursive(f, a, c, tol / 2.0, left) +
                    quad_recursive(f, c, b, tol / 2.0, right))
    
    # Initial whole estimate using Simpson's rule over the entire interval
    mid = (a + b) / 2.0
    initial_whole = (func(a) + 4 * func(mid) + func(b)) * (b - a) / 6.0
    
    return quad_recursive(func, a, b, tol, initial_whole)

# Example usage:
def example_function(x):
    return x**2 * math.sin(x)

# Integrating example_function from 0 to π with a tolerance of 1e-6
import math
a = 0
b = math.pi
result = adaptive_quadrature(example_function, a, b, tol=1e-6)
print(f"Integral result: {result}")
