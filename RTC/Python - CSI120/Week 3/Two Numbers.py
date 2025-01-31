import random

#Generate two random numbers between begin and end
#compare those numbers 
#expected output
#Enter begin of the range: 10
#Enter the end of the range: 20
#Generated Number-1:7
#Generated Number-2:9
#Number 9 is larger than number 7

#input begin of the range
begin_1 = int(input("Enter begin of the range: ")) #10
#input the end of the range
end_1 = int(input("Enter the end of the range: ")) #20
#Generated number
number_1 = random.randint(begin_1, end_1)
number_2 = random.randint(begin_1, end_1)

if number_1 > number_2:
    print(f"{number_1} is more than {number_2}.")
else:
    print(f"{number_2} is more than {number_1}.")