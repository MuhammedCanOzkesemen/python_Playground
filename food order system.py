menu = ["burger", "pizza", "pasta", "water"]

def order_system():
    orders = []
    print("Menu:", menu)

    while True:
        item = input("Choose a food (type 'done' to finish): ").lower()
        if item == "done":
            break
        elif item not in menu:
            print("This food is not in the menu.")
        elif item in orders:
            print("You already added this item.")
        else:
            orders.append(item)

    print("\nYour orders:")
    for i, food in enumerate(orders, start=1):
        print(f"{i}. {food}")
    print("Total items:", len(orders))

order_system()
