class Statement:
    def __init__(self):
        self.startingBalance = 0
        self.endingBalance = 0
        self.startDate = ""
        self.endDate = ""
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
