import re

def match_ab_zero_or_more(text):
    pattern = r'a[b]*'
    match = re.fullmatch(pattern, text)
    return match is not None

# Example usage
print(match_ab_zero_or_more("ab"))    # True
print(match_ab_zero_or_more("a"))     # True
print(match_ab_zero_or_more("abbbb")) # True
print(match_ab_zero_or_more("ac"))    # False