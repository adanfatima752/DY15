def complex_operations(c1, c2):
    try:
        # Unpacking the tuples into real and imaginary parts
        real1, imag1 = c1
        real2, imag2 = c2
        
        # Addition
        addition = (real1 + real2, imag1 + imag2)
        
        # Subtraction
        subtraction = (real1 - real2, imag1 - imag2)
        
        # Multiplication
        multiplication = (real1 * real2 - imag1 * imag2, real1 * imag2 + imag1 * real2)
        
        # Division (handling division by zero)
        denom = real2**2 + imag2**2
        if denom == 0:
            division = "Error: Division by zero"
        else:
            division = ((real1 * real2 + imag1 * imag2) / denom, (imag1 * real2 - real1 * imag2) / denom)
        
        # Returning the results
        return {
            'addition': addition,
            'subtraction': subtraction,
            'multiplication': multiplication,
            'division': division
        }
    
    except ValueError:
        return "Error: Invalid input, tuples must contain exactly two numbers each"
    except TypeError:
        return "Error: Invalid input, elements in the tuple must be numbers"

# Example usage
c1 = (1, 2)  # 1 + 2i
c2 = (3, 4)  # 3 + 4i

result = complex_operations(c1, c2)
print("Addition:", result['addition'])
print("Subtraction:", result['subtraction'])
print("Multiplication:", result['multiplication'])
print("Division:", result['division'])
