balance = 4842;
annualInterestRate = 0.2;
monthlyPaymentRate = 0.04
# Paste your code into this box
Monthly_interest = annualInterestRate / 12.0
paid = 0.0

for x in range(1, 13):
    Minimum_monthly_payment = monthlyPaymentRate * balance
    monthly_unpaid = balance - Minimum_monthly_payment
    paid += round(Minimum_monthly_payment, 1)
    print("Month:", x)
    print("Minimum monthly payment", round(Minimum_monthly_payment, 2))
    balance = monthly_unpaid + (Monthly_interest * monthly_unpaid)
    print("Remaining balance:", round(balance, 2))

print("Total paid:", paid)
print("Remaining balance:", round(balance, 1))
