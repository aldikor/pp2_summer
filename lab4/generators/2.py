def generate_even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

# Input from console
n = int(input("Enter a number: "))

# Generate and print even numbers
even_numbers = generate_even_numbers(n)
print("Even numbers:", ", ".join(map(str, even_numbers)))