def remove_item():
    code = int(input("Enter item code to remove: "))
    for item in menu:
        if item[0] == code:
            menu.remove(item)
            print("Item removed.")
            return
    print("Invalid code.")
