"""
Name: Sunlim Lee
Activity: Lab7
Date: 11/10/2021
Ask the user to enter a store's sales for each day of the week.
The sales will be stored in a list.
Use a loop to calculate the total of sales in the list and display the total
"""
print("Lab 7 Part 1: Sales Total")
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
daily_totals = []

for day in days:
    total = float(input("Enter sales amount for " + day + ": $"))
    daily_totals.append(total)
    
print(daily_totals)
print("Total of all sales: $" + str(sum(daily_totals)))
