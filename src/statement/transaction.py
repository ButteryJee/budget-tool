class Transaction:
    def __init__(self, date, memo, withdrawal, deposit, balance, category):
        self.date= date
        self.memo = memo
        self.withdrawal = withdrawal
        self.deposit = deposit
        self.balance = balance
        self.category = category
