import sys

inv = []

def display_menu():
    print("INVENTORY MANAGEMENT SYSTEM")
    print("1: Add an Item")
    print("2: Edit an Item")
    print("3: View Inventory")
    print("4: Remove an Item")
    print("5: Exit")
    choice = input("Please enter your selection: ")
    # .strip allows the choice to be interpreted even with whitespaces
    return choice.strip()

def main():
    while True:
        choice = display_menu()
        if choice == '5':
            print("Exiting Inventory Management System.")
            sys.exit(0)
        else:
            print("Invalid input. Please try again.")

main()
