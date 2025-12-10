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
