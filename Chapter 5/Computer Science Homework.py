def product_one():

    print("This is product one")

def product_two():

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
