#!/usr/bin/env python3

# display a welcome message
print("The Test Scores program")
print()
print("Enter 3 test scores")
print("======================")

# get scores from the user
#total_score = 0       # initialize the variable for accumulating scores
#total_score += int(input("Enter test score: "))
#total_score += int(input("Enter test score: "))
#total_score += int(input("Enter test score: "))

length = int(input("Please enter the length: "))
width = int(input("Please enter the width:  "))
#score3 = int(input("Enter test score: "))
#total_score = (score1 + score2 + score3)
area = (length * width)
perimeter = ((length*2)+(width*2))

# calculate average score
#average_score = round(total_score / 3)
             
# format and display the result
print("======================")
#print("Your Scores:  ",score1, score2, score3)
#print("Total Score:  ", total_score,
#      "\nAverage Score:", average_score)
print("Area      = ",area)
print("Perimeter = ",perimeter)
print()
print("Bye!")


