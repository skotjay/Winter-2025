# Display first ten natural odd numbers
# result = 1, 3, 5, 7, 9, 11, 13, 15, 17, 19

import os
os.system('cls')
counter = 1
loop_number = int(input("How many odd numbers do you want to display? "))
while counter <= 2 * loop_number:
    print(counter)
    counter += 2
