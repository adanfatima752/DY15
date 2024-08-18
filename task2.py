def evaluate_polynomial(coefficients, x):
    """
    Evaluate a polynomial at a given value of x.
    
    :param coefficients: List of coefficients for the polynomial. 
                         The list should start with the coefficient for the highest degree.
                         Example: [a, b, c, d] represents ax^3 + bx^2 + cx + d
    :param x: The value at which to evaluate the polynomial.
    :return: The result of the polynomial evaluation.
    """
    # Determine the degree of the polynomial
    degree = len(coefficients) - 1
    
    # Initialize the result to zero
    result = 0
    
    # Loop through the coefficients and calculate the polynomial value
    for i, coeff in enumerate(coefficients):
        # Calculate the power of x for the current term
        power = degree - i
        term_value = coeff * (x ** power)
        
        # Add the term value to the result
        result += term_value
        
        # Handle cases where the coefficient is zero
        if coeff == 0:
            print(f"Skipping term with coefficient 0 for x^{power}")
    
    return result

# Example usage:
# For a quadratic polynomial 3x^2 + 2x + 1, the coefficients are [3, 2, 1]
coefficients = [3, 2, 1]  # 3x^2 + 2x + 1
x_value = 5
result = evaluate_polynomial(coefficients, x_value)
print(f"The polynomial evaluated at x = {x_value} is: {result}")
