from file_handler import initialize_file, add_entry
from report import monthly_summary, export_report
from chart import generate_chart

def main():
    initialize_file()

    while True:
        print("===== Expense Tracker CLI =====")
        print("1. Add Entry")
        print("2. Monthly Summary")
        print("3. Export Monthly Report (CSV)")
        print("4. Generate Chart")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            monthly_summary()
        elif choice == "3":
            export_report()
        elif choice == "4":
            generate_chart()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main()