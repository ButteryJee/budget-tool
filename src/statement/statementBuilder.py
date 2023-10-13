from src.statement.statement import Statement
from src.statement.transactionFactory import *


class StatementBuilder:
    def __init__(self):
        self.statement = None
        self.transactionFactory = CreditUnionTransactionFactory()

    def get_statement(self):
        return self.statement

    def build(self, reader):
        self.statement = Statement()
        for i, row in enumerate(reader.get_rows()):
            transaction = self.transactionFactory.create(row)
            self.statement.add_transaction(transaction)
            if i == 0:
                self.statement.startDate = transaction.date
                self.statement.startingBalance = transaction.balance
            if i == len(reader.get_rows())-1:
                self.statement.endDate = transaction.date
                self.statement.endingBalance = transaction.balance
        self.statement.balanceChange = self.statement.startingBalance - self.statement.endingBalance
        print(self.statement.__dict__)