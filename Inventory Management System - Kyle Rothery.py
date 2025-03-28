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

def edit_inv():
    print("\n--- Edit an Item ---")
    # Ends the edit function if there are no items to edit
    if not inv:
        print("Inventory is empty. Nothing to edit.")
        return
    view_inv()
    edit_choice = input("Enter the item number to edit: ").strip()
    try:
        # Choice that user enters is subtracted by 1 as the list starts at 0
        edit_choice = int(edit_choice) - 1
        if edit_choice < 0 or edit_choice >= len(inv):
            print("Item number out of range.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    # Retrieves the item from the inventory
    item = inv[edit_choice]
    print(f"Editing item: {item['name']} (Current Quantity: {item['quantity']})")
    new_name = input("Enter new name (leave blank to keep current): ").strip()
    new_qty = input("Enter new quantity (leave blank to keep current): ").strip()
    # if loop necessary so that user can keep the same if they wish
    if new_name:
        item["name"] = new_name
    if new_qty:
        # try catch prevents invalid quantity being entered
        try:
            item["quantity"] = int(new_qty)
        except ValueError:
            print("Invalid quantity entered. Keeping previous quantity.")
    inv[edit_choice] = item
    print("Item updated successfully.")

def view_inv():
    print("\n--- Current Inventory ---")

def main():
    while True:
        choice = display_menu()
        if choice == '1':
            add_inv()
        elif choice == '2':
            edit_inv()
        elif choice == '3':
            view_inv()
        elif choice == '4':
            print("WORK IN PROGRESS")
        elif choice == '5':
            print("Exiting Inventory Management System.")
            sys.exit(0)
        else:
            print("Invalid input. Please try again.")

main()
