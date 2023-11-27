def door_lock_system(K, B):
    # Designing logic circuit using OR gate
    if K or B:
        return "Door unlocks"
    else:
        return "Door remains locked"

# Simulating the door lock system with different inputs
K = 1  # Valid key card swiped
B = 0  # Button not pressed
print(door_lock_system(K, B))  # Output: Door unlocks
