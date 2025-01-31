#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven = float(input("Enter miles driven:         "))
gallons_used = float(input("Enter gallons of gas used:  "))

if miles_driven <= 0:
    print("Miles driven must be greater than zero. Please try again.")
elif gallons_used <= 0:
    print("Gallons used must be greater than zero. Please try again.")
else:
    # calculate and display miles per gallon
    mpg = round(miles_driven / gallons_used, 2)
    print("Miles Per Gallon:          ", mpg)
    print()
    while True:
        another_calculation = input("Would you like to perform another calculation? (y/n): ").lower()
        if another_calculation == 'y':
            miles_driven = float(input("Enter miles driven:         "))
            gallons_used = float(input("Enter gallons of gas used:  "))

            if miles_driven <= 0:
                print("Miles driven must be greater than zero. Please try again.")
            elif gallons_used <= 0:
                print("Gallons used must be greater than zero. Please try again.")
            else:
                mpg = round(miles_driven / gallons_used, 2)
                print("Miles Per Gallon:          ", mpg)
                print()
        elif another_calculation == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
print("Bye!")



