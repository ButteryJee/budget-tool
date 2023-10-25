import matplotlib.pyplot as plt


def plot_statement_balance(statement, axes):
    colors = {"groceries": "k",
              "utilities": "k",
              "car": "k",
              "ignore": "k",
              "savings": "k",
              "household": "k",
              "gas": "k",
              "entertainment": "k",
              "rent": "k",
              "income": "k",
              "loans": "k",
              "health": "k"}
    x = []
    y = []
    c = []
    for i, transaction in enumerate(statement.transactions):
        x.append(i)
        y.append(transaction.balance)
        c.append(colors[transaction.category])
    axes.scatter(x, y, color=c, zorder=2, s=70)
    axes.set_ylabel("Balance [$]")
    axes.set_xlabel("Transaction Number")
    axes.set_title("Statement Balance")
    axes.grid(zorder=1)


def plot_income_spent(budget, axes):
    total = 0
    income = 0
    budgeted = 0
    for key in budget.categories.keys():
        if key == "income":
            income = income + budget.categories[key].spent
        else:
            total = total + abs(budget.categories[key].spent)
            budgeted = budgeted + budget.categories[key].budgeted
    # Add $500 for discretionary spending
    budgeted = budgeted + 500
    total = total + 500
    container = axes.bar(x="Income", height=income, zorder=2)
    axes.bar_label(container, fmt='${:,.0f}')
    container = axes.bar(x="Spent", height=total, zorder=2)
    axes.bar_label(container, fmt='${:,.0f}')
    container = axes.bar(x="Budgeted", height=budgeted, zorder=2)
    axes.bar_label(container, fmt='${:,.0f}')
    axes.grid(zorder=1)


def plot_pie_categories(budget, axes):
    labels = []
    sizes = []
    for key in budget.categories.keys():
        category = budget.categories[key]
        if key == "income":
            continue
        else:
            labels.append(key)
            sizes.append(abs(category.spent))
    axes.pie(sizes, labels=labels, autopct='%1.1f%%')

def plot_category_bar(budget, axes):
    for key in budget.categories.keys():
        if key == "income":
            continue
        else:
            category = budget.categories[key]
            if category.remaining < 0:
                color = "#d62728"
            elif category.remaining == 0:
                color = "#7f7f7f"
            else:
                color = "#2ca02c"
            container = axes.bar(x=key, height=abs(category.spent), color=color, zorder=2)
            axes.bar_label(container, fmt='${:.0f}\n'+"$"+str(int(category.budgeted)))
    for label in axes.get_xticklabels():
        label.set_rotation(45)
        label.set_ha('right')
    axes.grid(zorder=1)