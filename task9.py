import re

def evaluate_expression(expression, variables):
    try:
        # Replace variables in the expression with their values from the dictionary
        for var, value in variables.items():
            expression = re.sub(rf'\b{var}\b', str(value), expression)

        # Check for any undefined variables
        undefined_vars = re.findall(r'[a-zA-Z_]\w*', expression)
        if undefined_vars:
            return f"Error: Undefined variables found: {', '.join(undefined_vars)}"

        # Safely evaluate the expression
        result = eval(expression, {"__builtins__": None}, {})
        return result
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage
variables = {'x': 10, 'y': 5, 'z': 2}
expression = "3 * x + y / z - a"
result = evaluate_expression(expression, variables)
print(result)  # Output: Error: Undefined variables found: a

expression2 = "3 * x + y / z"
result2 = evaluate_expression(expression2, variables)
print(result2)  # Output: 32.5
