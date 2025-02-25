import os
os.system('cls')
n = int(input("Enter n: "))

def is_prime(num):
    if num < 2:
        return False
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            return False
        divisor += 1
    return True

count = 0
num = 2

while count < n:
    if is_prime(num):
        print(num)
        count += 1
    num += 1