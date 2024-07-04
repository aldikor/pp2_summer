def countdown(n):
    for i in range(n, -1, -1):
        yield i

# Example usage
n = 5
countdown_generator = countdown(n)
print(f"Countdown from {n} to 0:")
for number in countdown_generator:
    print(number)