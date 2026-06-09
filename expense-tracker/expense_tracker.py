expenses = []

amount = input("Enter expense: ")
amount = float(amount)

expenses.append(amount)

amount = input("Enter expense: ")
amount = float(amount)

expenses.append(amount)

amount = input("Enter expense: ")
amount = float(amount)

expenses.append(amount)

total=sum(expenses)

print("Total expenses: ",total)