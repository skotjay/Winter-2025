def calculate_interest_rate(principal, final_amount, time_period):
    interest = final_amount - principal
    interest_rate = (interest / principal) / time_period
    return interest_rate * 100

def main():
    time_unit = input("Choose the time unit (months/years): ").strip().lower()
    if time_unit not in ["months", "years"]:
        print("Invalid time unit. Please choose either 'months' or 'years'.")
        return

    try:
        time1 = int(input(f"Enter the first time period in {time_unit}: "))
        time2 = int(input(f"Enter the second time period in {time_unit}: "))
        if time1 >= time2:
            print("The second time period must be greater than the first.")
            return

        principal = float(input("Enter the initial dollar amount: "))
        final_amount = float(input("Enter the final dollar amount: "))
        if principal <= 0 or final_amount <= 0:
            print("Dollar amounts must be positive.")
            return

        time_period = time2 - time1
        if time_unit == "months":
            time_period /= 12  # Convert months to years

        interest_rate = calculate_interest_rate(principal, final_amount, time_period)
        print(f"The interest rate is {interest_rate:.2f}% per year.")
    except ValueError:
        print("Invalid input. Please enter numeric values for time periods and dollar amounts.")

if __name__ == "__main__":
    main()