def generate_squares(n):
    for i in range(n + 1):
        yield i * i

# Example usage
N = 5
squares_generator = generate_squares(N)
print(f"Squares up to {N}:")
for square in squares_generator:
    print(square)