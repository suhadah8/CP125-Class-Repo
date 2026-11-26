# Lab 01 Exercise 1: Road Trip Budgeter
def is_budget_sufficient(one_way_km,budget):
    total_distance = one_way_km * 2
    fuel_needed = total_distance / 10
    fuel_cost = fuel_needed * 2

    return bool(budget >= fuel_cost) 

print(is_budget_sufficient(100,40))
print(is_budget_sufficient(100,39))