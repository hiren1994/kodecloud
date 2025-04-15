import math

# Function to calculate the area of a circle
def calculate_area(radius):
    return math.pi * (radius ** 2)

# Input: Get the radius from the user
radius = float(input("Enter the radius of the circle: "))

# Output: Display the area
area = calculate_area(radius)
print(f"The area of the circle with radius {radius} is {area:.2f}")
