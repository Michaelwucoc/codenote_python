def garage_system(V, C):
    # Designing logic circuit using OR gate
    if V or C:
        return "Garage door opens/closes"
    else:
        return "Garage door remains in its current state"

# Simulating the garage system with different inputs
V = 1  # Vehicle is detected
C = 0  # Remote control not activated
print(garage_system(V, C))  # Output: Garage door opens/closes
