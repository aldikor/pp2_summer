def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

# Example usage
a = 2
b = 5
squares_generator = squares(a, b)
print(f"Squares from {a} to {b}:")
for square in squares_generator:
    print(square)