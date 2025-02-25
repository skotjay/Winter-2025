#Accept inpute from user and generate random number. Break from the loop as soon as random matches with the number provided by the user.
import random
num = int(input("Enter a number 1-10: "))
counter = 1
while True:
    rand = random.randint(1, 10)
    counter += 1
    print(rand, end=" ")
    if rand == num:
        break
print("Random number: ", rand)
print("Input", num)