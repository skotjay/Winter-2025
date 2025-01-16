# Start of the program

# Step 1: Read the temperature from the user
temperature = float(input("Enter the temperature in degrees: "))

# Step 2: Check the conditions based on the flowchart
if temperature > 100:
    print("It's too hot!")
elif 60 <= temperature <= 99:
    print("I guess this will do.")
elif temperature < 60:
    print("This is fine!")