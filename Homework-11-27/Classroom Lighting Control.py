def lighting_control_system(P, D, S):
    # Designing logic circuit using AND, OR, and NOT gates
    if (P and not D) or S:
        return "Lights turn on"
    else:
        return "Lights remain off"

# Simulating the lighting control system with different inputs
P = 1  # Presence detected
D = 0  # Daylight is sufficient
S = 1  # Manual switch is ON
print(lighting_control_system(P, D, S))  # Output: Lights turn on
