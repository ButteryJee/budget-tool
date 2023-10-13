from src.statement.transaction import Transaction


class CreditUnionTransactionFactory:
    def __init__(self):
        self.dateKey = "Date"
        self.withdrawalKey = "Amount Debit"
        self.depositKey = "Amount Credit"
        self.balanceKey = "Balance"
        self.memoKey = "Memo"

    def create(self, row):
        date = row[self.dateKey]
        memo = row[self.memoKey]
        withdrawal = self.string_to_float(row[self.withdrawalKey])
        deposit = self.string_to_float(row[self.depositKey])
        balance = self.string_to_float(row[self.balanceKey])
        return Transaction(date, memo, withdrawal, deposit, balance)

    def string_to_float(self, text):
        if text == "":
            return 0.0
        else:
            return float(text)