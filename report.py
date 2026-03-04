import csv

FILE_NAME = "expenses.csv"

def monthly_summary():
    month = input("Enter month (YYYY-MM): ")
    total_income = 0
    total_expense = 0

    with open(FILE_NAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Date"].startswith(month):
                if row["Type"] == "Income":
                    total_income += float(row["Amount"])
                else:
                    total_expense += float(row["Amount"])

    print("\n--- Monthly Summary ---")
    print("Total Income :", total_income)
    print("Total Expense:", total_expense)
    print("Net Savings  :", total_income - total_expense)
    print("------------------------\n")

    return total_income, total_expense

def export_report():
    month = input("Enter month to export (YYYY-MM): ")
    output_file = f"report_{month}.csv"

    with open(FILE_NAME, mode='r') as file, \
         open(output_file, mode='w', newline='') as out_file:

        reader = csv.DictReader(file)
        writer = csv.DictWriter(out_file, fieldnames=reader.fieldnames)
        writer.writeheader()

        for row in reader:
            if row["Date"].startswith(month):
                writer.writerow(row)

    print(f"Report exported as {output_file}\n")