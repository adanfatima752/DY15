import re
from datetime import datetime

def extract_dates(text):
    # Regular expression to match dates in "YYYY-MM-DD" format
    date_pattern = r'\b(\d{4})[-/](\d{2})[-/](\d{2})\b'
    
    # Find all matches in the text
    matches = re.findall(date_pattern, text)
    
    valid_dates = []
    
    for match in matches:
        year, month, day = match
        
        # Check if the date is valid
        try:
            date_str = f"{year}-{month}-{day}"
            datetime.strptime(date_str, "%Y-%m-%d")
            valid_dates.append(date_str)
        except ValueError:
            # Invalid date
            continue
    
    return valid_dates

# Example usage
text = "Here are some dates: 2023-12-31, 2024/02/30, 2022-01-01."
dates = extract_dates(text)
print(dates)  # Output: ['2023-12-31', '2022-01-01']
