def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def main():
    principal = input("Enter the initial principal (or 'answer' to solve for it): ")
    rate = input("Enter the interest rate (or 'answer' to solve for it): ")
    time = input("Enter the number of months (or 'answer' to solve for it): ")
    balance = input("Enter the account balance (or 'answer' to solve for it): ")

    if principal.lower() == 'answer':
        rate = float(rate)
        time = float(time)
        balance = float(balance)
        principal = balance / (1 + (rate * time) / 100)
        print(f"The initial principal is: {principal:.2f}")
    elif rate.lower() == 'answer':
        principal = float(principal)
        time = float(time) / 12
        balance = float(balance)
        rate = (balance / principal - 1) * (100 / time)
        print(f"The interest rate is: {rate:.2f}%")
    elif time.lower() == 'answer':
        principal = float(principal)
        rate = float(rate)
        balance = float(balance)
        time = (balance / principal - 1) * (100 / rate)
        print(f"The number of years is: {time:.2f}")
    elif balance.lower() == 'answer':
        principal = float(principal)
        rate = float(rate)
        time = float(time)
        balance = principal * (1 + (rate * time) / 100)
        print(f"The account balance is: {balance:.2f}")
    else:
        print("Invalid input. Please enter 'answer' for one of the values to solve for it.")

if __name__ == "__main__":
    main()
