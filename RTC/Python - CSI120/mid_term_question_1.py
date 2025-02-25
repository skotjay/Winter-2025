#User enter years_of_service as integer.
years_of_service = int(input("Enter Years of Service: "))

#User enters current_salary as float.
current_salary = float(input("Enter Current Salary: "))

# Calculate bonus_percentage based on years_of_service
if years_of_service < 3:
    bonus_percentage = 0
elif years_of_service <= 5:
    bonus_percentage = 10
elif years_of_service <= 10:
    bonus_percentage = 20
else:
    bonus_percentage = 30

# Calculate bonus_amount and total_salary after bonus
bonus_amount = current_salary * (bonus_percentage / 100)
total_salary = current_salary + bonus_amount

# Display the results
print(f"Bonus: {bonus_percentage}%")
print(f"Bonus Amount: ${bonus_amount}")
print(f"Total Salary after Bonus: ${total_salary}")
