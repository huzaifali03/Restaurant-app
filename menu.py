def show_menu():
    print("\n--- MENU ---")
    print("Code   Item            Price")
    for item in menu:
        print(item[0], "   ", item[1], "       ", item[2])
