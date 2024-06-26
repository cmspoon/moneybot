class Checking:
    _details = {}
    def __init__(self, name, amt, dep, prd, rate): 
        self.name = name
        self.amt = amt
        self.dep = dep
        self.prd = prd
        self.rate = rate
        self.save = amt
        Checking._details[self.name] = self
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
    def retrieve(cls, name):
        if name in cls._details:
            return cls._details[name].calculate()
        else:
            return f"Account with name '{name}' not found."

def main():
    while True:
        print("\nThe Money Maker:")
        print("1. Create a new checking account")
        print("2. View an existing checking account by name")
        print("3. Exit")
        choice = input('Choose an option: ')
        if choice == "1":
            try:
                name = input("What is the name of your checking account? ")
                amt = round(float(input('How much money is in the checking account? (Ex. "2500") ')), 2)
                dep = float(input('How much is the monthly contribution? (Ex. "80") '))
                prd = int(input('How long of a period, in years? (Ex. "5") '))
                rate = float(input('What is the account\'s APY? (Ex. "4.25") '))
                account = Checking(name, amt, dep, prd, rate)
                print(account.calculate())
            except ValueError:
                print("\nInvalid input. Please enter numeric values for amount, contribution, period, and rate.")
        elif choice == "2":
            name = input("Enter the name of the checking account to view: ")
            print(Checking.retrieve(name))
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
