from src.budget.budgetCategory import BudgetCategory
from src.budget.budgetAmounts import BUDGET_AMOUNTS


class Budget:
    def __init__(self):
        self.spending = {}
        self.categories = {}

    def update_spending(self, statement):
        for transaction in statement.transactions:
            category = transaction.category
            if category == "ignore":
                continue
            if category not in self.categories.keys():
                self.categories[category] = BudgetCategory()
            self.categories[category].add_spending(transaction.withdrawal + transaction.deposit)
            self.categories[category].budgeted = BUDGET_AMOUNTS[category]
            self.categories[category].update_remaining()

    def print_categories(self):
        for key in self.categories.keys():
            category = self.categories[key]
            print("{}:".format(key))
            print("\tSpent: {}".format(category.spent))
            print("\tRemaining: {}".format(category.remaining))

    def update_budget(self, budgetFile):
        pass