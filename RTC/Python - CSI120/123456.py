#Print three while loops of numbers.
import os
os.system('clear')
i = 0
c = 11
while i < 3:
    j = 0
    while j <= 3:
        print(c, end = " ")
        c += 11
        j += 1
    print("\n")
    i += 1