# Lab 01 Exercise 4: Dynamic Parking Rate
def get_hourly_rate(vehicle_type, hour):
    if vehicle_type == "Electric":
        rate = 2
    elif vehicle_type == "Hybrid":
        if ((hour>21 and hour<24) or (hour >= 0 and hour < 7)):
            rate = 2
        else :
            rate = 5
    else:
        rate = 5
    return rate

print (get_hourly_rate("Hybrid", 23))
print (get_hourly_rate("Hybrid", 13))
print (get_hourly_rate("Sedan", 2))