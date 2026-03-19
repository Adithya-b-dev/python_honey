

income=float(input("Enter your annual income: "))
tax=0
if income<=250000:
    tax=0
elif income<=500000:
    tax=(income-250000)*0.05
elif income<=1000000:
    tax=(250000*0.05)+(income-500000)*0.20
else:
    tax=(250000*0.05)+(500000*0.20)+(income-1000000)*0.30
print("Income Tax to be paid: Rs.",tax)



def calculate_compound_interest():
    print("Compound Interest Investment Growth Calculator")

    while True:
        try:
            initial_amount = float(input("Enter the initial investment amount (e.g., 1000): "))
            if initial_amount >= 0:
                break
            else:
                print("Investment must be a positive number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    while True:
        try:
            annual_rate_percent = float(input("Enter the annual interest rate (in percentage, e.g., 5 for 5%): "))
            if annual_rate_percent >= 0:
                break
            else:
                print("Interest rate must be a positive number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        try:
            years = int(input("Enter the number of years: "))
            if years > 0:
                break
            else:
                print("Number of years must be a positive integer. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid whole number for years.")

    current_amount = initial_amount

    print("\nInvestment Growth Summary:")
    print("-" * 23)
    print(f"{'Year':<5}{'Amount':>15}")
    print(f"{'-' * 5}{'-' * 15}")

    for year in range(1, years + 1):

        interest_gained = current_amount * (annual_rate_percent / 100)
        current_amount += interest_gained

        print(f"{year:<5}{current_amount:>15.2f}")

    print("-" * 23)
    print(f"Final Value after {years} years: ${current_amount:.2f}")

calculate_compound_interest()

     




     
