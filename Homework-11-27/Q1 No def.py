import time
K = int (input("Enter the K value (0 means off, 1 means on)"))
B = int (input("Enter the B value (0 means off, 1 means on)"))
unlock = 0

if K or B:
    unlock=1
else:
    unlock=0

if unlock:
    print ("The door unlocked")
    for _ in range(10):
        print("#######Unlocked######\nQuit in 10 seconds")
        time.sleep(1)
        
        