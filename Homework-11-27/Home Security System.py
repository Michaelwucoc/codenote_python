def home_security_system(W, D):
    # Designing logic circuit using OR gate
    if W or D:
        return "Alarm activates"
    else:
        return "No alarm activation"

# Simulating the home security system with different inputs
W = int (input("Please enter the W value.(0 means off, 1 means on) \n"))  # Window closed
D = int (input("Please enter the D value.(0 means off, 1 means on) \n"))  # Door opened
print(home_security_system(W, D))  # Output: Alarm activates
