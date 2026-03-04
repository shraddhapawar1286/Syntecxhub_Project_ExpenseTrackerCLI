import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Type", "Category", "Amount"])

def add_entry():
    date_input = input("Enter date (YYYY-MM-DD): ")
    try:
        datetime.strptime(date_input, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format!")
        return

    entry_type = input("Enter type (Income/Expense): ").capitalize()
    if entry_type not in ["Income", "Expense"]:
        print("Invalid type!")
        return

    category = input("Enter category: ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount!")
        return

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date_input, entry_type, category, amount])

    print("Entry added successfully!\n")