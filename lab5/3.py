import re

def find_lowercase_underscore(text):
    pattern = r'[a-z]+_[a-z]+'
    matches = re.findall(pattern, text)
    return matches

# Example usage
print(find_lowercase_underscore("this_is_a_test")) # ['this_is', 'a_test']
print(find_lowercase_underscore("test_no_match"))  # ['test_no']