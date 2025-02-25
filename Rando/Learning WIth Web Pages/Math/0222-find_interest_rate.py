#Print "Let's find the interest rate.
print("Let's find the interest rate.")
#Ask the user to choose the time unit (months/years) and assign it to time_unit
time_unit = input("Choose the time unit (months/years): ").strip().lower()
#If time_unit is not in ["months", "years"]:
if time_unit not in ["months", "years"]:
    #Print "Invalid time unit. Please choose either 'months' or 'years'."
    print("Invalid time unit. Please choose either 'months' or 'years'.")
    #Exit the program
    quit()
#Ask the user to enter the first time period in time_unit and assign it to time1
time1 = int(input(f"Enter the first time period in {time_unit}: "))
#Ask the user to enter the second time period in time_unit and assign it to time2
time2 = int(input(f"Enter the second time period in {time_unit}: "))
#If time1 is greater than or equal to time2:
if time1 >= time2:
    #Print "The second time period must be greater than the first."
    print("The second time period must be greater than the first.")
    #Exit the program
    quit()
#Ask the user to enter the initial dollar amount and assign it to principal
account_balance = float(input("Enter the initial dollar amount: "))
#Ask the user to enter the final dollar amount and assign it to final_amount
final_amount = float(input("Enter the final dollar amount: "))
#If principal is less than or equal to 0 or final_amount is less than or equal to 0:
if account_balance <= 0 or final_amount <= 0:
    #Print "Dollar amounts must be positive."
    print("Dollar amounts must be positive.")
    #Exit the program
    quit()
    
#Print "First we find the difference between the final amount and the principal."
interest = final_amount - account_balance
print()
print(f"First we caculate interest earned by subracting first account balance (${account_balance:.2f}) from the second (${final_amount:.2f}). To calculate that the amount of interest earned is ${interest:.2f}")

#ask the user to press the "Enter" key to continue
print()
input("Press Enter to continue...")

#Print "Next we find the time period between the two time periods."
time_period = time2 - time1
print ()
print(f"Next we subtract {time1} from {time2} to calculate that the amount of time elapsed is {time_period} {time_unit}.")

#ask the user to press the "Enter" key to continue
print()
input("Press Enter to continue...")

interest_per_month = interest / time_period
print()
print(f"Then divide the amount of interest gained (${interest:.2f}) by the amount of time passed ({time_period} {time_unit}) to calculate the interest per {time_unit}. Which turns out to be ${interest_per_month:.2f}")

#ask the user to press the "Enter" key to continue
print()
input("Press Enter to continue...")

#We will take a moment to calculate the starting value.
starting_interest = time1 * interest_per_month
starting_balance = account_balance - starting_interest

print()
print(f"Now that we know the amount of interest per month (${interest_per_month:.2f}), we can calculate the account's starting balance by taking the starting time value of {time1} {time_unit} and multipling it by the interest per month (in this example ${interest_per_month:.2f}, to find out how much interest (${starting_interest}) was accumulated in that time.")

print()
input("Press Enter to continue...")


print()
print(f"Now we will then subtract from the starting account balance (${starting_interest:.2f}) to find the starting value (${starting_balance:.2f}).")

print()
print(f"...starting value is ${starting_balance:.2f}")

#ask the user to press the "Enter" key to continue
print()
input("Press Enter to continue...")
print(f"To find the annual interest rate, we will divide the interest per month (${interest_per_month:.2f}) by the starting value (${starting_balance:.2f}) and multiply by 100.")

#ask the user to press the "Enter" key to continue
print()
input("Press Enter to continue...")
