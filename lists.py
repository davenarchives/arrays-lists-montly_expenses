print("Montly Expenses:")
months = ["January", "February", "March", "April", "May"]
monthly_expenses = [5200, 6350, 4600, 4130, 3190]

for i in range(len(months)):
    print(f"{months[i]}: Php{monthly_expenses[i]}")

#1. In Feb,how many pesos you spent extra compare to January?
extra_expenses = monthly_expenses[1] - monthly_expenses[0]
print(f"\n1. Extra Expenses: Php{extra_expenses}")

#2. Find out your total expense in first quarter(first three months) of the year.
first_quarter_expense = sum(monthly_expenses[:3])
print(f"2. First Quarter Expense: Php{first_quarter_expense}")

#3. Find out if you spend exactly 2000 pesos in any month
for expenses in range(len(monthly_expenses)):
    if monthly_expenses[expenses] == 2000:
        print(f"3. Yes you spent exactly 2000 in {months[expenses]}.")
        break
else:
    print("3. No, you did not spend exactly 2000 in any month.")

#4. June month just finished and your expense is 1980 pesos. Add this item to our monthly expenses list
june_expense = 1980
months.append("June")
monthly_expenses.append(june_expense)

print("\n4. Updated Monthly Expenses:")
for i in range(len(months)):
    print(f"{months[i]}: Php{monthly_expenses[i]}")

#5. You returned an item that you brought in a month of April and got a refund of 200 pesos
april_refund = months.index("April")
monthly_expenses[april_refund] -= 200

print("\n5. Updated Monthly Expenses after refund:")
for i in range(len(months)):
    print(f"{months[i]}: Php{monthly_expenses[i]}")
