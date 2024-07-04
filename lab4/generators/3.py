def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Example usage
n = 100
divisible_generator = divisible_by_3_and_4(n)
print(f"Numbers divisible by 3 and 4 up to {n}:")
for number in divisible_generator:
    print(number)