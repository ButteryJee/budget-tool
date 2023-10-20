import csv
import os

TEMP_FILE = "temp/temp_csv.csv"


class CsvReader:
    def __init__(self, filename, skiprows):
        self.headers = []
        self.rows = []
        self.filename = filename
        self.skiprows = skiprows
        self.read_file()

    def read_file(self):
        self.preprocess()
        with open(TEMP_FILE, newline="") as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader):
                self.rows.append(row)
            f.close()
        self.remove_temp()

    def preprocess(self):
        with open(self.filename, "r") as f:
            with open(TEMP_FILE, "w+") as out:
                text = f.read()
                lineList = text.split("\n")
                for line in lineList[self.skiprows:]:
                    out.write(line+"\n")
                out.close()
            f.close()

    def remove_temp(self):
        os.remove(TEMP_FILE)

    def get_rows(self):
        return self.rows
