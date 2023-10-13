from src.statement.statementBuilder import StatementBuilder


class StatementDirector:
    def __init__(self):
        self.statementBuilder = StatementBuilder()

    def build_statement(self, csvReader):
        self.statementBuilder.build(csvReader)
        return self.statementBuilder.get_statement()
