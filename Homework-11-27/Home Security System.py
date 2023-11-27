def home_security_system(W, D):
    # Designing logic circuit using OR gate
    if W or D:
        return "Alarm activates"
    else:
        return "No alarm activation"

# Simulating the home security system with different inputs
W = 0  # Window closed
D = 1  # Door opened
print(home_security_system(W, D))  # Output: Alarm activates
