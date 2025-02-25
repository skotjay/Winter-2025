import os
os.system('clear')

for i in range(1): #skip all number that are divisible by 5
    if i % 5 == 0:
        continue
    print(i, end=" ")

counter = 0
num = 1
total = 30
while counter < total:
    if num % 5 == 0:
        num += 1
        continue
    print(num, end=" ")
    num += 1
    counter += 1
print(num, end = " ")

print("\nTotal numbers: ", counter)
