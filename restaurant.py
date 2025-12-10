menu = [
    [1, "Idly", 30],
    [2, "Dosa", 40],
    [3, "Fried Rice", 120],
    [4, "Veg Burger", 80]
]

def show_menu():
    print("\n--- MENU ---")
    print("Code   Item            Price")
    for item in menu:
        print(item[0], "   ", item[1], "       ", item[2])

def add_item():
    code = int(input("Enter item code: "))
    name = input("Enter item name: ")
    price = int(input("Enter price: "))
    menu.append([code, name, price])
    print("Item added successfully.")

def update_item():
    code = int(input("Enter item code to update: "))
    for item in menu:
        if item[0] == code:
            name = input("Enter new name: ")
            price = int(input("Enter new price: "))
            item[1] = name
            item[2] = price
            print("Item updated.")
            return
    print("Invalid code.")

def remove_item():
    code = int(input("Enter item code to remove: "))
    for item in menu:
        if item[0] == code:
            menu.remove(item)
            print("Item removed.")
            return
    print("Invalid code.")

def generate_bill():
    total = 0
    print("\nEnter item codes (0 to stop):")
    while True:
        code = int(input("Item code: "))
        if code == 0:
            break
        
        # Search without using a 'found' flag
        for item in menu:
            if item[0] == code:
                qty = int(input("Quantity: "))
                total += item[2] * qty
                break
        else:
            print("Invalid code!")

    print("\n--- BILL ---")
    print("Total Amount:", total)
    print("Thank you! Visit again.")

def main():
    while True:
        print("\n1. Show Menu")
        print("2. Add Item")
        print("3. Update Item")
        print("4. Remove Item")
        print("5. Generate Bill")
        print("6. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            show_menu()
        elif choice == 2:
            add_item()
        elif choice == 3:
            update_item()
        elif choice == 4:
            remove_item()
        elif choice == 5:
            generate_bill()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

main()
