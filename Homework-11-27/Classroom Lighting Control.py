def lighting_control_system(P, D, S):
    # Designing logic circuit using AND, OR, and NOT gates
    if (P and not D) or S:
        return "Lights turn on"
    else:
        return "Lights remain off"

# Simulating the lighting control system with different inputs
P = int (input("Please enter the P value.(0 means off, 1 means on) \n"))  # Presence detected
D = int (input("Please enter the D value.(0 means off, 1 means on) \n"))  # Daylight is sufficient
S = int (input("Please enter the S value.(0 means off, 1 means on) \n"))  # Manual switch is ON
print(lighting_control_system(P, D, S))  # Output: Lights turn on
