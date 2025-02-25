#print three rows of three stars using nested loops only.
import os
os.system('clear')
stars = 0

while stars < 3:
    star_loop = 0
    while star_loop < 3:
        print("*", end = "     ")
        star_loop += 1
    print("\n")
    stars+=1