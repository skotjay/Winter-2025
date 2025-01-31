#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
cost_gallon = float(input("Enter cost per gallon:\t\t"))
total_cost = float(cost_gallon * gallons_used)
cost_per_mile = float(total_cost/miles_driven)

# calculate miles per gallon
mpg = round(miles_driven / gallons_used, 1)

# format and display the result
print()
print(f"Miles Per Gallon:\t\t{mpg}")
print(f"Total cost:\t\t\t{total_cost}")
print(f"Cost per Mile:\t\t\t{cost_per_mile}")
print()
print("Bye!")


