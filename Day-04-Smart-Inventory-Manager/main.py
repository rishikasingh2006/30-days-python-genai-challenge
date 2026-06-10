inventory = {}
categories = set()

for i in range(3):

    product = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    category = input("Enter category: ")

    inventory[product] = quantity
    categories.add(category)

print("\nInventory:\n")

for product, quantity in inventory.items():

    print(product, ":", quantity)

    if quantity < 3:
        print("Low Stock Alert!")