"""
CP1404/CP5632 Practical
Cumulative total income program using a single function
"""

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_months = int(input("How many months? "))  # Using meaningful variable name

    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))  # Using f-string for input
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, num_months + 1):
        income = incomes[month - 1]
        total += income

        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()
