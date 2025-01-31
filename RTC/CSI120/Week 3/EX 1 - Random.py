# Check if a random number is even or odd
import random
number = random.randint(1, 100)
print(f"System generated number is {number}: ")
if number % 2 == 0:
    print("Number is even.")
else:
    print("Number is odd.")

    