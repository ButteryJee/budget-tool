class BudgetCategory:
    def __init__(self):
        self.budgeted = 0.00
        self.spent = 0.00
        self.remaining = 0.00

    def add_spending(self, amount):
        self.spent = round(self.spent + amount, 2)

    def update_remaining(self):
        self.remaining = round(self.budgeted + self.spent, 2)
