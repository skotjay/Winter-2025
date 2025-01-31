#Generate two numbers between x and y and accept another range, if the generated numbers are in the range, print the numbers, otherwise print the message "Numbers are not in the range"
import random

#input begin of the range
begin_1 = int(input("Enter begin of the range: ")) #100
#input the end of the range
end_1 = int(input("Enter the end of the range: ")) #1000
#Generated number
number = random.randint(begin_1, end_1) #number = random.randint(100, 1000)

#input begin of the range
begin_2 = int(input("Enter begin of the range: ")) #100
#input the end of the range
end_2 = int(input("Enter the end of the range: ")) #1000

if number >= begin_2 and number <= end_2:
    print(f"The generated number is {number}, and is in the range")
else:
    print(f"The number is {number} not in the range")
    