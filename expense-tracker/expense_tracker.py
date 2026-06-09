# Create an empty list that stores expense ammounts
expenses = []

# Ask the user for three expenses and add them to the list [1-3]
amount = input("Enter expense 1: ")
amount = float(amount)
expenses.append(amount)

amount = input("Enter expense 2: ")
amount = float(amount)
expenses.append(amount)

amount = input("Enter expense 3: ")
amount = float(amount)
expenses.append(amount)

# Calculate the total cost of all expenses + print the result
total= sum(expenses)
print("Total expenses:",total)

# Count how many expenses were entered + print the result
expense_count = len(expenses)
print("Number of expenses:",expense_count)

# Calculate the average expense + print the result
average = total / expense_count
print("Average expense:",average)
