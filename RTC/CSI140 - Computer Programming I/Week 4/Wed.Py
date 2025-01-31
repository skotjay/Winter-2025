choice = "y"

while choice.lower() == 'y':
    customer_name = input("Enter customer name:")
    product_name = input("Product Name: ")
    quantity = input("Quantity: ")
    price = input("Price: ")
    total_price = int(quantity) * int(price)
    print(f"Customer {customer_name} bought {quantity} {product_name}s for {total_price}")
    choice = input("Do you wish to continue? (y/n)")

print("Have a nice day!")

#properly validated means that it has to be fully validated