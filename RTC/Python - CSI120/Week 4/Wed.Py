#Name the variable and set the stage to run.
choice = "y"

while choice.lower() == 'y':

    #The same essential loop structure repeated.

    #naming the variable to set the conditions for the loop.
    #Begin the while loop by checking current conditions.
        #User Input based on condition.
        #Input validation
            #Error Handling

    customer_name = ""
    while customer_name == "":
        customer_name = input("Enter customer name:")
        if customer_name == "":
            print("Please enter valid name: ")

    product_name = ""
    while product_name == "":
        product_name = input("Enter product name:")
        if product_name == "":
            print("Please enter valid name: ")

    quantity = 0
    while quantity <= 0:
        quantity = int(input("Quantity: "))
        if quantity <= 0:
            print("Please enter valid quantity.")
            
    price = 0
    while price <= 0:
        price = int(input("Price: "))
        if price <= 0:
            print("Please enter valid price.")

    total_price = quantity * price
    print(f"Customer {customer_name} bought {quantity} {product_name}s for ${total_price}")
    choice = input("Do you wish to continue? (y/n)")

print("Have a nice day!")