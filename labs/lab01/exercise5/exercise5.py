# Lab 01 Exercise 5: Triangle Checker
def is_valid_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

print (is_valid_triangle(3, 4, 5))
print (is_valid_triangle(1, 2, 3))