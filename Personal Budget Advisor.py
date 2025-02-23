import os

class BudgetAdvisor:
    def __init__(self):
        self.income = 0
        self.expenses = []
        self.expense_categories = {}

    def input_income(self):
        while True:
            try:
                self.income = float(input("Enter your monthly income: $"))
                if self.income < 0:
                    raise ValueError("Income cannot be negative.")
                break
            except ValueError as e:
                print(f"Error: {e}. Please enter a valid income.")

    def input_expenses(self):
        print("Enter your expenses (type 'done' to finish):")
        while True:
            category = input("Enter expense category (e.g., 'Food', 'Rent', 'Utilities'): ").strip()
            if category.lower() == 'done':
                break
            try:
                amount = float(input(f"Enter amount for {category}: $"))
                if amount < 0:
                    raise ValueError("Expense amount cannot be negative.")
                if category in self.expense_categories:
                    self.expense_categories[category] += amount
                else:
                    self.expense_categories[category] = amount
            except ValueError as e:
                print(f"Error: {e}. Please enter a valid expense.")

    def analyze_spending(self):
        total_expenses = sum(self.expense_categories.values())
        savings = self.income - total_expenses
        savings_percentage = (savings / self.income) * 100 if self.income > 0 else 0
        print("\nSpending Analysis:")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Savings: ${savings:.2f}")
        print(f"Savings Percentage: {savings_percentage:.2f}%")
        for category, amount in self.expense_categories.items():
            category_percentage = (amount / total_expenses) * 100 if total_expenses > 0 else 0
            print(f"{category}: ${amount:.2f} ({category_percentage:.2f}%)")

    def budget_suggestions(self):
        total_expenses = sum(self.expense_categories.values())
        if total_expenses > self.income:
            print("\nWarning: You are spending more than your income. Consider cutting back on expenses.")
        elif total_expenses > self.income * 0.8:
            print("\nYou're spending a lot relative to your income. Consider saving more.")
        else:
            print("\nGreat job! You're spending within a reasonable budget.")

        if self.income > 0:
            food_expense = self.expense_categories.get('Food', 0)
            if food_expense > self.income * 0.2:
                print("Consider reducing your food expenses to save more money.")

    def save_data(self):
        try:
            with open("budget_data.txt", "w") as f:
                f.write(f"Income: ${self.income:.2f}\n")
                f.write("Expenses:\n")
                for category, amount in self.expense_categories.items():
                    f.write(f"{category}: ${amount:.2f}\n")
            print("\nData saved successfully.")
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self):
        if os.path.exists("budget_data.txt"):
            try:
                with open("budget_data.txt", "r") as f:
                    lines = f.readlines()
                    self.income = float(lines[0].strip().split(": $")[1])
                    self.expense_categories = {}
                    for line in lines[2:]:
                        category, amount = line.strip().split(": $")
                        self.expense_categories[category] = float(amount)
                print("\nData loaded successfully.")
            except Exception as e:
                print(f"Error loading data: {e}")
        else:
            print("\nNo saved data found.")

    def display_menu(self):
        while True:
            print("\nPersonal Budget Advisor Menu:")
            print("1. Input Income")
            print("2. Input Expenses")
            print("3. Analyze Spending")
            print("4. Get Budget Suggestions")
            print("5. Save Data")
            print("6. Load Data")
            print("7. Exit")
            choice = input("Enter your choice (1-7): ")
            if choice == '1':
                self.input_income()
            elif choice == '2':
                self.input_expenses()
            elif choice == '3':
                self.analyze_spending()
            elif choice == '4':
                self.budget_suggestions()
            elif choice == '5':
                self.save_data()
            elif choice == '6':
                self.load_data()
            elif choice == '7':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    advisor = BudgetAdvisor()
    advisor.display_menu()