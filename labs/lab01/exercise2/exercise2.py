# Lab 01 Exercise 2: Camping Logistics
import math 
def calculate_tent_cost(participant,tent_capacity,tent_price):
    tent_amount = math.ceil(participant / tent_capacity)
    total_cost = tent_amount * tent_price
    return total_cost

print(calculate_tent_cost(12,4,100))
print(calculate_tent_cost(13,4,100))