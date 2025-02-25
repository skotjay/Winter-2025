
import os
os.system('cls')
counter = int(input('How many prime numbers would you like? '))
count = 1
print("2\n")

while count < counter:
       if num % 2 == 0 and num % 3 == 0 and num % 5 == 0 and num % 7 == 0:
         flag = True
         break   
       i=i+1    
    if flag == False:
        print(num)
    num = num + 1
    count = count + 1