def product_one():
    # Function for the first product
    # Add the functionality for the first product here
    print("This is product one")

def product_two():
    # Function for the second product
    # Add the functionality for the second product here
    print("This is product two")

def main():
    print("Welcome to the shop!")
    choice = input("Enter 1 for product one or 2 for product two: ") 
    if choice == "1":
        product_one()  
    elif choice == "2":
        product_two()
    else:
        print("Invalid choice")

main()
