import matplotlib.pyplot as plt


def plot_statement_balance(statement):
    x = []
    y = []
    for i, transaction in enumerate(statement.transactions):
        x.append(i)
        y.append(transaction.balance)
    plt.scatter(x, y)
    plt.ylabel("Balance [$]")
    plt.xlabel("Transaction Number")
    plt.title("Statement Balance")
    plt.show()
