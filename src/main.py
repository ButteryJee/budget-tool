from src.statement import *
from plot import *


STATEMENT_FILE = "data/2023-october.csv"
STATEMENT_SKIP_ROWS = 3

if __name__ == "__main__":
    reader = CsvReader(STATEMENT_FILE, STATEMENT_SKIP_ROWS)
    statementDirector = StatementDirector()
    statement = statementDirector.build_statement(reader)

    plot_statement_balance(statement)