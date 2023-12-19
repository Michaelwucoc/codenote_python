import math

# Define the coordinates of the two points
point1 = (1, 2)
point2 = (5, 8)

# Calculate the difference in x and y coordinates
dx = point2[0] - point1[0]
dy = point2[1] - point1[1]

# Calculate the distance using the Pythagorean theorem
distance = math.sqrt(dx**2 + dy**2)

# Print the distance as a square root
print(f"The distance between the two points is approximately {distance:.2f}")

# Alternatively, you can use the math.dist() function for a more concise approach:

# distance = math.dist(point1, point2)

# Print the distance with the square root symbol
print(f"The distance between the two points is approximately √{distance:.2f}")
