import re

def split_at_uppercase(text):
    return re.split(r'(?=[A-Z])', text)

# Example usage
print(split_at_uppercase("SplitAtUppercaseLetters")) # ['Split', 'At', 'Uppercase', 'Letters']