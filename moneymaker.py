class Account:
    _details = {}
    def __init__(self, name, amt, dep, prd, rate): 
        self.name = name
        self.amt = amt
        self.dep = dep
        self.prd = prd
        self.rate = rate
        self.save = amt
        Account._details[self.name] = self
    
    def calculate(self):
        monthly_rate = self.rate / 100 / 12
        months = self.prd * 12
        for _ in range(months):
            self.save = (self.save + self.dep) * (1 + monthly_rate)
        self.save = round(self.save, 2)
        interest_earned = round(self.save - self.amt - (self.dep * months), 2)
        total_deposits = self.amt + (self.dep * months)
        return (f"\n{self.name}\n"
                f"Initial Balance: ${self.amt}\n"
                f"Monthly Contribution: ${self.dep}\n"
                f"Period: {self.prd} Years\n"
                f"APY: {self.rate}%\n"
                f"Interest Earned: ${interest_earned}\n"
                f"Total Contributions: ${total_deposits}\n"
                f"Total Balance: ${self.save}")

    @classmethod
    def retrieve(cls):
        return list(cls._details.keys())
    
    @classmethod
    def edit(cls, name, amt, dep, prd, rate):
        if name in cls._details:
            account = cls._details[name]
            account.amt = amt
            account.dep = dep
            account.prd = prd
            account.rate = rate
            account.save = amt
            return f"Account '{name}' updated successfully."
        else:
            return f"Account with name '{name}' not found."

def main():
    while True:
        print("\nThe Money Maker:")
        print("1. Create a new account")
        print("2. View an existing account")
        print("3. Edit an existing account")
        print("4. Exit")
        choice = input('Choose an option: ')
        
        if choice == "1":
            try:
                name = input("What is the name of the account? ")
                amt = round(float(input('How much money is in the account? (Ex. "2500") ')), 2)
                dep = float(input('How much is the monthly contribution? (Ex. "80") '))
                prd = int(input('How long of a period, in years? (Ex. "5") '))
                rate = float(input('What is the account\'s APY? (Ex. "4.25") '))
                account = Account(name, amt, dep, prd, rate)
                print(account.calculate())
            except ValueError:
                print("\nInvalid input. Please enter numeric values for amount, contribution, period, and rate.")

        elif choice == "2":
            account_names = Account.retrieve()
            if account_names:
                print("Existing accounts:")
                for index, account_name in enumerate(account_names, start=1):
                    print(f"{index}. {account_name}")
                selection = input("Enter the number of the account to view: ")
                try:
                    selection_index = int(selection) - 1
                    if 0 <= selection_index < len(account_names):
                        selected_account_name = account_names[selection_index]
                        print(Account._details[selected_account_name].calculate())
                    else:
                        print("Invalid selection. Please enter a valid number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                print("No accounts found.")

        elif choice == "3":
            account_names = Account.retrieve()
            if account_names:
                print("Existing accounts:")
                for index, account_name in enumerate(account_names, start=1):
                    print(f"{index}. {account_name}")
                selection = input("Enter the number of the account to edit: ")
                try:
                    selection_index = int(selection) - 1
                    if 0 <= selection_index < len(account_names):
                        selected_account_name = account_names[selection_index]
                        try:
                            amt = round(float(input('Enter the new amount: ')), 2)
                            dep = float(input('Enter the new monthly contribution: '))
                            prd = int(input('Enter the new period in years: '))
                            rate = float(input('Enter the new APY: '))
                            print(Account.edit(selected_account_name, amt, dep, prd, rate))
                        except ValueError:
                            print("\nInvalid input. Please enter numeric values for amount, contribution, period, and rate.")
                    else:
                        print("Invalid selection. Please enter a valid number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                print("No accounts found.")

        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
