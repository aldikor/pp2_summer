import math

def regular_polygon_area(num_sides, side_length):
    apothem = side_length / (2 * math.tan(math.pi / num_sides))
    return (num_sides * side_length * apothem) / 2

# Input values
num_sides = 4
side_length = 25
area = regular_polygon_area(num_sides, side_length)
print(f"Input number of sides: {num_sides}")
print(f"Input the length of a side: {side_length}")
print(f"The area of the polygon is: {area:.2f}")