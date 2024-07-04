import re

def match_ab_two_to_three(text):
    pattern = r'a[b]{2,3}'
    match = re.fullmatch(pattern, text)
    return match is not None

# Example usage
print(match_ab_two_to_three("abb"))   # True
print(match_ab_two_to_three("abbb"))  # True
print(match_ab_two_to_three("abbbb")) # False
print(match_ab_two_to_three("a"))     # False