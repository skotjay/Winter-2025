#First, the user inputs their grade.
score = int(input("Enter test score: "))

#See if Score is within valid range (0-100).
if score <=100 and score >=0:
    #check if student passed or failed the class
    if score >=73:
        print("Passed:")
    if score <=72:
        print("Fail:")
else:
    print("Out of range")