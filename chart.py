import matplotlib.pyplot as plt
from report import monthly_summary

def generate_chart():
    income, expense = monthly_summary()

    labels = ['Income', 'Expense']
    values = [income, expense]

    plt.figure()
    plt.bar(labels, values)
    plt.title("Monthly Income vs Expense")
    plt.xlabel("Type")
    plt.ylabel("Amount")
    plt.savefig("monthly_chart.png")
    plt.close()

    print("Chart saved as monthly_chart.png\n")