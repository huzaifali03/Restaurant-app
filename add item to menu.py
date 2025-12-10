def add_item():
    code = int(input("Enter item code: "))
    name = input("Enter item name: ")
    price = int(input("Enter price: "))
    menu.append([code, name, price])
    print("Item added successfully.")
