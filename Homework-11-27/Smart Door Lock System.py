def door_lock_system(K, B):
    # Designing logic circuit using OR gate
    if K or B:
        return "Door unlocks"
    else:
        return "Door remains locked"

# Simulating the door lock system with different inputs
K = int (input("Please enter the K value.(0 means off, 1 means on) \n"))  # Valid key card swiped
B = int (input("Please enter the B value.(0 means off, 1 means on) \n"))  # Button not pressed
print(door_lock_system(K, B))  # Output: Door unlocks
