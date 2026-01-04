print("--This is Expense Burnout Calculator--")

# Data
amount = float(input("Enter Your Investment(RS): "))
expenses = {
    "Rent": 15000,
    "Salaries": 40000,
    "CloudSaaS": 5000,
    "Marketing": 10000
}

# Calculate monthly expenses
monthly_burn = sum(expenses.values())
print(f"Total Monthly Burn: {monthly_burn} RS")

months = 0
current_balance = amount

print("\n--- Monthly Runway Forecast ---")
while current_balance >= monthly_burn:
    current_balance -= monthly_burn
    months += 1
    # :2f rounds to 2 decimal places, , adds commas for thousands
    print(f"Month {months}: Remaining Balance = {current_balance:,.2f} RS")
    
print(f"\nCritical: You will run out of cash in {months} months.")   

# LOGIC: Check for danger first
if months < 6:
    print("WARNING: Low Runway! Suggestion: Pivot your product or seek funding.")
elif months < 12:
    print("STABLE: Keep monitoring your burn rate & focus on growth.")
else:
    print("HEALTHY: You have over a year of runway!")