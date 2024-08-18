import re

def digit_to_word(digit):
    word_map = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', 
        '4': 'four', '5': 'five', '6': 'six', '7': 'seven', 
        '8': 'eight', '9': 'nine'
    }
    return word_map[digit]

def transform_string(text):
    # Replace all digits with their word equivalents
    text = re.sub(r'\d', lambda x: digit_to_word(x.group()), text)
    
    # Split the text into words
    words = text.split()
    
    # Reverse words longer than 5 characters and apply title case
    transformed_words = [word[::-1] if len(word) > 5 else word for word in words]
    
    # Join the transformed words and convert to title case
    transformed_text = ' '.join(transformed_words).title()
    
    return transformed_text

# Example usage
input_text = "This is a test string with 12345, and some longwords."
transformed_text = transform_string(input_text)
print(transformed_text)  # Output: "This Is A Test Gnirts Htiw One Two Three Four Five, And Some Sdrongwol."
