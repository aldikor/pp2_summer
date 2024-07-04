import re

def insert_spaces_capital(text):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)

# Example usage
print(insert_spaces_capital("InsertSpacesBetweenWords")) # "Insert Spaces Between Words"