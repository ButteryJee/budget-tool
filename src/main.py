from src.statement import *
from src.budget import *
from plot import *
import matplotlib.pyplot as plt


STATEMENT_FILE = "data/2023-october.csv"
STATEMENT_SKIP_ROWS = 3

if __name__ == "__main__":
    reader = CsvReader(STATEMENT_FILE, STATEMENT_SKIP_ROWS)
    statementDirector = StatementDirector()
    statement = statementDirector.build_statement(reader)
    budget = Budget()
    budget.update_spending(statement)
    budget.print_categories()


    fig, ax = plt.subplots(1, 3, figsize=(18,8))
    plot_statement_balance(statement, ax[0])
    plot_income_spent(budget, ax[1])
    plot_category_bar(budget, ax[2])
    plt.show()