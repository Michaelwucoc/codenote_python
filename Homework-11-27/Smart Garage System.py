def garage_system(V, C):
    # Designing logic circuit using OR gate
    if V or C:
        return "Garage door opens/closes"
    else:
        return "Garage door remains in its current state"

# Simulating the garage system with different inputs
V = int (input("Please enter the V value.(0 means off, 1 means on) \n"))  # Vehicle is detected
C = int (input("Please enter the C value.(0 means off, 1 means on) \n"))  # Remote control not activated
print(garage_system(V, C))  # Output: Garage door opens/closes
