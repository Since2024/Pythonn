print("--This is Expense Burnout Calculator--")

#Data
amount = float(input("Enter Your Investment(RS): "))
expenses ={
    "Rent": 15000,
    "Salaries": 40000,
    "CloudSaaS": 5000,
    "Marketing": 10000
}

#Calculate monthly expenses
monthly_burn = sum(expenses.values())
print(f"Total Monthly Burn: {monthly_burn} RS")

months = 0
current_balance = amount

print("\n---MOnthly Runway forcast---")
while current_balance >= monthly_burn:
    current_balance -= monthly_burn
    months += 1
    print(f"Month {months}: Remaining Balance = {current_balance:,.2f} RS")
    
print(f"\nCritical: You will run out of cash in {months} months.")   

if month > 6:
    print("WArning: LOw Runway! Suggestion: Pivot your product or Seek funding immediately.")
elif months >= 12:
    print("Healthy:YOu have over a year of runway.")
else:
    print("Stable: Keep monitoring your BUrn rate & focus on growth.")     
