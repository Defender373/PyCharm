balance = 4773
annualInterestRate = 0.2
Monthly_interest = annualInterestRate / 12.0

for payment in range(0, balance, 10):
    initial_balance = balance
    for j in range(1, 13):
        initial_balance -= payment
        initial_balance += Monthly_interest * initial_balance
    if initial_balance <= 0:
        print("Lowest Payment: ", payment)
        break
