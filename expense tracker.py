def welcome_message():
  print("Welcome to the Expense Tracker!")
  print("Welcome to the Expense Tracker")
    
def log_expense():
    while True:
        try:
            amount = float(input("Enter the expense amount: "))
            if amount <= 0:
                print("Amount should be positive.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    category = input("Enter the expense category (e.g., Food, Transport, Entertainment): ").strip()
    description = input("Enter a description of the expense: ").strip()

    return {"amount": amount, "category": category, "description": description}

expenses = []

def add_expense():
    expense = log_expense()
    expenses.append(expense)
    print("Expense added successfully!")

def display_summary():
    total_spent = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal amount spent: {total_spent}")

    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        category_totals[category] = category_totals.get(category, 0) + expense["amount"]

    print("\nTotal spent by category:")
    for category, total in category_totals.items():
        print(f"{category}: {total}")

    print("\nAll expenses:")
    for expense in expenses:
        print(f"{expense['category']} - {expense['description']}: {expense['amount']}")

def thank_you_message():
    print("\nThank you for using the Expense Tracker!")

def main():
    welcome_message()
    while True:
        print("\nOptions:")
        print("1. Log an expense")
        print("2. Display summary")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            display_summary()
        elif choice == "3":
            thank_you_message()
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()