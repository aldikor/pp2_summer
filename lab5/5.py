import re

def match_a_anything_b(text):
    pattern = r'a.*b$'
    match = re.fullmatch(pattern, text)
    return match is not None

# Example usage
print(match_a_anything_b("a123b")) # True
print(match_a_anything_b("ab"))    # True
print(match_a_anything_b("a"))     # False
print(match_a_anything_b("b"))     # False