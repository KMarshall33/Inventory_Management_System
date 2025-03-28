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

def add_inv():
    print("\n--- Add an Item ---")
    name = input("Enter the name of the item: ").strip()
    qty_input = input("Enter the quantity: ").strip()
    try:
        qty = int(qty_input)
    except ValueError:
        print("Invalid quantity. Please enter a valid number.")
        return
    # Create a new item dictionary and add it to the inventory
    item = {"name": name, "quantity": qty}
    inv.append(item)
    print(f"Item '{name}' added with quantity {qty}.")

def main():
    while True:
        choice = display_menu()
        if choice == '1':
            add_inv()
        elif choice == '2':
            print("WORK IN PROGRESS")
        elif choice == '3':
            print("WORK IN PROGRESS")
        elif choice == '4':
            print("WORK IN PROGRESS")
        elif choice == '5':
            print("Exiting Inventory Management System.")
            sys.exit(0)
        else:
            print("Invalid input. Please try again.")

main()
