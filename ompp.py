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
        self.save = self.amt
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

    def future_balance(self, years):
        monthly_rate = self.rate / 100 / 12
        months = years * 12
        balance = self.amt
        for _ in range(months):
            balance = (balance + self.dep) * (1 + monthly_rate)
        return round(balance, 2)

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
    
    @classmethod
    def portfoilo(cls):
        account_names = cls.retrieve()
        if not account_names:
            return "No accounts found."
        print("Available accounts:")
        for index, account_name in enumerate(account_names, start=1):
            print(f"{index}. {account_name}")
        selected_indices = input("Enter the numbers of the accounts to include in portfolio creation (comma-separated): ")
        try:
            selected_indices = [int(i) - 1 for i in selected_indices.split(",")]
        except ValueError:
            return "Invalid input. Please enter valid numbers."
        selected_accounts = [account_names[i] for i in selected_indices if 0 <= i < len(account_names)]
        if not selected_accounts:
            return "No valid accounts selected."
        total_net_worth = 0
        total_net_worth_5_years = 0
        total_net_worth_10_years = 0
        summary = "\nCurrent Portfolio:\n"
        for account_name in selected_accounts:
            account = cls._details[account_name]
            total_net_worth += account.amt  # Calculate based on initial balance
            total_net_worth_5_years += account.future_balance(5)
            total_net_worth_10_years += account.future_balance(10)
            summary += (f"\n{account_name}:\n"
                        f"  Starting Balance: ${account.amt}\n"
                        f"  APY: {account.rate}%\n")
        total_net_worth = round(total_net_worth, 2)
        total_net_worth_5_years = round(total_net_worth_5_years, 2)
        total_net_worth_10_years = round(total_net_worth_10_years, 2)
        summary += (f"\nCurrent Net Worth: ${total_net_worth}\n"
                    f"5-Year Net Worth: ${total_net_worth_5_years}\n"
                    f"10-Year Net Worth: ${total_net_worth_10_years}\n")
        return summary

def main():
    while True:
        print("\nWelcome to moneybot 💵")
        print("1. Create a new account")
        print("2. View an existing account")
        print("3. Edit an existing account")
        print("4. Create a portfilo")
        print("5. Exit")
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
            summary = Account.portfoilo()
            print(summary)

        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
