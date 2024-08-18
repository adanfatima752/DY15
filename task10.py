import re

def validate_entries(data_entries):
    report = []

    for entry in data_entries:
        entry_report = {'entry': entry, 'length': None, 'content': None, 'format': None}

        # Validate length (e.g., should be between 5 and 20 characters)
        if 5 <= len(entry) <= 20:
            entry_report['length'] = "Pass"
        else:
            entry_report['length'] = "Fail"

        # Validate content (alphabetic, numeric, alphanumeric)
        if entry.isalpha():
            entry_report['content'] = "Alphabetic"
        elif entry.isdigit():
            entry_report['content'] = "Numeric"
        elif entry.isalnum():
            entry_report['content'] = "Alphanumeric"
        else:
            entry_report['content'] = "Invalid content"

        # Validate format (email, date)
        if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", entry):
            entry_report['format'] = "Email"
        elif re.match(r"^\d{4}-\d{2}-\d{2}$", entry):
            entry_report['format'] = "Date"
        else:
            entry_report['format'] = "Unknown format"

        report.append(entry_report)

    return report

# Example usage
data_entries = [
    "john.doe@example.com",
    "2024-08-11",
    "hello123",
    "short",
    "thisisaverylongentrythatexceedstwentycharacters",
    "12345",
    "invalid-email@.com",
    "notadate",
    "2023-02-30"
]

validation_report = validate_entries(data_entries)
for item in validation_report:
    print(item)
