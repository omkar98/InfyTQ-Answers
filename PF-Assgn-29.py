#PF-Assgn-29
"""
LOGIC:
    expenses = (distance/milege)*fuel_cost
    income = price_head * no_of_passengers
"""
def calculate(distance,no_of_passengers):
    fuel_cost = 70
    milege = 10
    price_head = 80
    expenses = (distance/milege)*fuel_cost
    income = price_head * no_of_passengers
    
    if income>=expenses:
        return income-expenses
    else:
        return -1

distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))
