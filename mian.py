import pandas as pd
import csv
from datetime import datetime

class CSV:
    CSV_FILES = "finanace_data.csv"
    COLUMNS = ["date","amount","category","description"]

    @classmethod
    def initilize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILES)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILES,index=False)
    
    @classmethod
    def add_entry(cls,date,amount,category,description):
        new_entry = {
            "date" : date,
            "amount" : amount,
            "category" : category,
            "description" : description,
            }
        with open(cls.CSV_FILES,"a",newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully!")
            
        

CSV.initilize_csv()
CSV.add_entry("23-07-2024",125.65,"Income","Salary")