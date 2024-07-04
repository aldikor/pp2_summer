import re

def find_upper_followed_by_lower(text):
    pattern = r'[A-Z][a-z]+'
    matches = re.findall(pattern, text)
    return matches

# Example usage
print(find_upper_followed_by_lower("Abc Xyz Test")) # ['Abc', 'Xyz', 'Test']
print(find_upper_followed_by_lower("aBc"))          # []