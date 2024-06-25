def checkings_menu():
    print("Welcome to the Money Tracker")
    account = int(input('How much money is in the checkings account? (Ex. "2500") '))
    deposit = int(input('How much is the monthly contribution? (Ex. "80") '))
    period = int(input('How long of a period, in years? (Ex. "5") '))
    rate = float(input("What is the account's APY?"' (Ex. "0.59") '))
    savings = account
    if deposit == 0:
        while period != 0:
            savings = round((savings) * (1 + rate), 2)
            period -= 1
    else: #accurate monthly depositing calculations
        skip   
    return(print(f"Over a period of {period} years, your inital deposit of ${account} turns into ${savings}"))

checkings_menu()