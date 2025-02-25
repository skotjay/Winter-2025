#user inputs {exam_score}
exam_score = int(input("Enter your exam score: "))

#validate the input, if {exam_score} is outside 0-100, print "Invalid input. Please enter a score between 0 and 100."
if exam_score < 0 or exam_score > 100:
    print("Invalid input. Please enter a score between 0 and 100.")
else:
    #calculate {grade} based on {exam_score}
    if exam_score >= 90:
        grade = "A - Excellent!"
    elif exam_score >= 80:
        grade = "B - Good Job!"
    elif exam_score >= 70:
        grade = "C - You Passed!"
    elif exam_score >= 60:
        grade = "D - Needs improvement!"
    else:
        grade = "F - Failed. Try Again!"
    #print {grade}
    print(grade)