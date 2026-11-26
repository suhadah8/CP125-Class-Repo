# Lab 01 Exercise 3: Secure Vault System
def validate_entry(name, pin):
    return bool( (name == "Director" and pin == 1122) or (name == "Security" and pin == 9900) )

print (validate_entry("Director", 1122))
print (validate_entry("Director", 9900))
print (validate_entry("director", 1122))