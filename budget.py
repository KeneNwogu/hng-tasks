class Budget:
    # Hard-coded total balance
    budget_balance = int(input("Enter your budget for the year: "))
    budgets = [] # stores a static list of all instances of the Budget class

    def __init__(self, category: str, balance: int):
        self.category = category
        # deducts balance from budget and stores as instance's balance
        if Budget.budget_balance > balance:
            Budget.budget_balance -= balance
            self.balance = balance
        else:
            print(f"WARNING: Can not set balance of {self.category} because Budget's balance is currently less than amount you plan to put into this category. It wil be set to a default balance of 0 \n")
            self.balance = 0
        Budget.budgets.append(self)

    def withdraw(self, amount):
        # withdraw budget from category to the general budget balance
        if self.balance > amount:
            Budget.budget_balance += amount
            self.balance -= amount
            print(f"Successfully withdrawn {amount} from {self.category} to the Main Budget")
            return True
        else:
            print('Can not perform this operation')
            return False

    @staticmethod
    def deposit(budget, amount):
        # deposit amount from the general budget balance to the category's balance
        # returns None if category is non-existent
        if amount <= Budget.budget_balance:
            Budget.budget_balance -= amount
            budget.balance += amount
            print(f"Successfully Deposited {amount} from the Main Budget to the {budget.category} balance")
            return budget.balance
        else:
            return 'None'

    @staticmethod
    def print_budget():
        print(f'General Budget Balance: {Budget.budget_balance} ')
        for budget in Budget.budgets:
            print(f'{budget.category}: {budget.balance}')
        print(f'Total Budget: {Budget.total()}')
    
    @staticmethod
    def transfer(budget_1, budget_2, amount):
        # Transfers amount from one category to the other

        # First withdraws from the category to the Main Budget
        can_withdraw = budget_1.withdraw(amount)
        if can_withdraw:
            # Deposits money transferred from budget_1 (to Main balance) to budget 2
            print(f"Successfully transferred {amount} from {budget_1.category} to {budget_2.category}")
            Budget.deposit(budget_2, amount)
    
    @staticmethod
    def total():
        # Gets total Budget
        total = 0
        total += Budget.budget_balance
        for budget in Budget.budgets:
            total += budget.balance
        return total

food = Budget('food', 50000) 
clothing = Budget('clothing', 45000)
entertainment = Budget('entertainment', 2000)
electricity = Budget('electricity', 100000)

# Takes 78 from the Main budget and adds it to food
Budget.deposit(food, 78)

# puts 78 into the general budget
food.withdraw(100)

# Transfer 40,000 to clothing's budget from food
Budget.transfer(food, clothing, 40000)

# won't be able to transfer because food's budget is lesser than amount to be transferred
Budget.transfer(food, electricity, 20000)

# Transfer 20,000 to food's budget from electricity
Budget.transfer(electricity, food, 20000)

# would now be able to transfer because food's budget is greater than 20000
Budget.transfer(food, electricity, 20000)

print("\n \n")
Budget.print_budget()     