import re

def replace_space_comma_dot(text):
    pattern = r'[ ,.]'
    result = re.sub(pattern, ':', text)
    return result

# Example usage
print(replace_space_comma_dot("Hello, world. This is a test.")) # "Hello:world:This:is:a:test:"