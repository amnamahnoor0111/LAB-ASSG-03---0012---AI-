# Shopping Program

products_list = []


def calculate_bill(products):
    bill = 0

    for p in products:
        bill = bill + p["total"]

    if bill > 10000:
        discount = bill * 0.10
    else:
        discount = 0

    final_bill = bill - discount

    return bill, discount, final_bill


for i in range(5):

    print("Product", i + 1, "write the product details :")

    name = input("Enter Product Name: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))

    total_price = price * quantity

    product_data = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "total": total_price
    }

    products_list.append(product_data)

    print()


print(" Products Details ")

file_text = "Shopping Bill\n\n"

for p in products_list:

    print("Product:", p["name"])
    print("Price:", p["price"])
    print("Quantity:", p["quantity"])
    print("Total Price:", p["total"])
    print()

    file_text = file_text + "Product: " + p["name"] + "\n"
    file_text = file_text + "Price: " + str(p["price"]) + "\n"
    file_text = file_text + "Quantity: " + str(p["quantity"]) + "\n"
    file_text = file_text + "Total Price: " + str(p["total"]) + "\n"
    file_text = file_text + "\n"


bill, discount, final_bill = calculate_bill(products_list)


expensive_product = products_list[0]

for p in products_list:

    if p["price"] > expensive_product["price"]:
        expensive_product = p


print("Complete Bill:", bill)
print("Discount:", discount)
print("Final Bill:", final_bill)

print("\nMost Expensive Product:", expensive_product["name"])
print("Price:", expensive_product["price"])


file_text = file_text + "\nComplete Bill: " + str(bill)
file_text = file_text + "\nDiscount: " + str(discount)
file_text = file_text + "\nFinal Bill: " + str(final_bill)
file_text = file_text + "\nMost Expensive Product: " + expensive_product["name"]


f = open("bill.txt", "w")
f.write(file_text)
f.close()

print("\nBill bill.txt file is saved !")