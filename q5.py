# Restaurant Program

menu = {
    1: {"name": "Burger", "price": 500},
    2: {"name": "Pizza", "price": 800},
    3: {"name": "Fries", "price": 250},
    4: {"name": "Drink", "price": 150}
}

orders = []


def calculate_bill(orders):
    bill = 0

    for order in orders:
        bill = bill + order["total"]

    return bill


print(" Restaurant Menu ")
print("1. Burger - Rs. 500")
print("2. Pizza - Rs. 800")
print("3. Fries - Rs. 250")
print("4. Drink - Rs. 150")


while True:

    choice = int(input("\nSelect item (0 to finish): "))

    if choice == 0:
        break

    if choice in menu:

        quantity = int(input("Enter Quantity: "))

        name = menu[choice]["name"]
        price = menu[choice]["price"]

        total_price = price * quantity

        order_data = {
            "name": name,
            "price": price,
            "quantity": quantity,
            "total": total_price
        }

        orders.append(order_data)

        print(name, "added to order.")

    else:
        print("Invalid item.")


bill = calculate_bill(orders)


print("\n Final Bill ")

file_text = "Restaurant Order\n\n"

for order in orders:

    print(order["name"], "x", order["quantity"], "=", order["total"])

    file_text = file_text + order["name"] + " x " + str(order["quantity"])
    file_text = file_text + " = Rs. " + str(order["total"]) + "\n"


print("\nFinal Bill:", bill)

file_text = file_text + "\nFinal Bill: Rs. " + str(bill)


f = open("orders.txt", "w")
f.write(file_text)
f.close()

print("\nOrder orders.txt file is saved !")