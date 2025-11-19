
def calculate_emi(principal, annual_rate, years):
    R = annual_rate / 12 / 100
    N = years * 12
    EMI = (principal * R * (1 + R)**N) / ((1 + R)**N - 1) #formula for loan interst
    total_payment = EMI * N
    total_interest = total_payment - principal
    return EMI, total_payment, total_interest

# Taking input from the user
P = float(input("Enter loan amount: "))
annual_rate = float(input("Enter annual interest rate (1-30%): "))
years = int(input("Enter loan tenure in years: "))
income = float(input("Enter your monthly income: "))


#  check if a user enter valid information
if annual_rate <= 0 or annual_rate > 30:
    print("Invalid interest rate!")
    exit()

if years < 1 or years > 30:
    print("Invalid loan tenure!")
    exit()

if P <= 0:
    print("Loan amount must be positive!")
    exit()


# Calculation of EMI

EMI, total_payment, total_interest = calculate_emi(P, annual_rate, years)

# Checking loam affordability
if EMI > 0.4 * income:
    print("\nWarning: EMI exceeds 40% of your income! Consider reducing loan amount or extending tenure.")
else:
    print("\nLoan seems affordable.")

#  Output

print(f"\nMonthly EMI: {EMI:.2f}")
print(f"Total Payment: {total_payment:.2f}")
print(f"Total Interest: {total_interest:.2f}")

'''our program is ready to calculate your 
 Annual interst, Monthly EMI,Total payment, Total interst'''
