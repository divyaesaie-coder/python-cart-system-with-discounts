#Cart system with discounts

items = {
    "Milk": 30,
    "Bread": 25,
    "Rice": 60,
    "Sugar": 45,
    "Eggs": 70,
    "Oil": 120,
    "Soap": 35,
    "Shampoo": 90,
    "Biscuits": 20,
    "Tea Powder": 110
}

cart = []
total = 0

while True:
    print("\n1) Buy items")
    print("2) View Total")
    print("3) Exit")
    ch = input("Choose: ")

    if ch == "1":
        print(items)
        item = input("Enter item name: ")

        if item in items:
            quantity = int(input("Enter quantity: "))
            price = items[item]

            bill = price * quantity
            total += bill

            cart.append((item, quantity))
            print("Added to cart!")
        else:
            print("Item not available!")

    elif ch == "2":
        print("Subtotal:", total)

        discount = 0

        # 10% discount if total > 1000
        if total > 1000:
            discount += total * 0.10

        # Extra 5% if 5+ items
        if len(cart) >= 5:
            discount += total * 0.05

        final = total - discount

        if final < 0:
            final = 0

        print("Discount:", discount)
        print("Final Bill:", final)

    elif ch == "3":
        print("Thank you!!")
        break

