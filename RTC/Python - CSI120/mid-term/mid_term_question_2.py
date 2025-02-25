import random

#Generate a random 2 Digit {lottery_number} (between 10 and 99)
lottery_number = random.randint(10, 99)

#User enters a 2 Digit {guess}
guess = int(input("Enter your 2 digit guess: "))

#print "Lottery Number was: {lottery_number}"
print(f"Lottery Number was: {lottery_number}")

#program validates that {guess} is 2 digits, no more or less.
if guess < 10 or guess > 99:
    print("Invalid Guess. Please enter a 2 digit number.")
#Program compares {guess} with {lottery_number}
else:
    if guess == lottery_number:
        print("Congratulations! You won $10,000!")
    elif sorted(str(guess)) == sorted(str(lottery_number)):
        print("Great job! You won $5,000!")
    elif any(digit in str(lottery_number) for digit in str(guess)):
        print("Good try! You won $1,000!")
    else:
        print("Sorry, better luck next time!")


	#if Same digits, same order = "Congratulations! You won $10,000!"
	#Same digits, different order = "Great job! You won $5,000!"
	#One matching digit = "Good try! You won $1,000!"
	#No matching digit = "Sorry, better luck next time!"
