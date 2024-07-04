import re

def camel_to_snake(camel_str):
    snake_str = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()
    return snake_str

# Example usage
print(camel_to_snake("thisIsATestString")) # "this_is_a_test_string"