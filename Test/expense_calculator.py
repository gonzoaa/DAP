import numpy as np
from random import random 

# Monthly Income
Income = 5000

# Expenses 
Rent = 1500
Groceries = 400
PG_E = 65
Car = 300
Gym = 30
other = 350

# Define a certain amount you want to save up for 
Target = 20000
savings = 0

Expenses  = np.array([Rent,Groceries , PG_E, Car, Gym])

# estimates monthly savings including random expenses 
def estimate (Expenses,Target,Income):
    total_expenses = np.sum(Expenses)
    ideal_savings_per_month = Income - total_expenses
    # account for random expenses 
    error = random()*random()*ideal_savings_per_month
    monthly_savings = ideal_savings_per_month - error
    return monthly_savings

months = []
months.append(0)
number_months = 0; 

# Adds up projected monthly savings until you reach your target amount 
while (savings < Target):
    f = estimate(Expenses,Target,Income) # call estimate function 
    savings = savings + f
    months.append(f)
    number_months = number_months +1
    

# Display Data
print('number of months until you hit your target saving = ', number_months)  
