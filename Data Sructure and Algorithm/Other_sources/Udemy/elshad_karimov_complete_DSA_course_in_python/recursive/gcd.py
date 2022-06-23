# GCD = The Largest positive integer that divides the numbers without a remainder
# Euclidean Algorithm
# To find: gcd(48,18)
# Step 1: 48/18 = quotient 2 and remainder 12
# Step 2: 18/12 = quotient 1 and remainder 6
# Step 3: 12/6 =  quotient 2 and remainder 0
# So, gcd(48,18) = 6

def gcd(num1: int, num2: int) -> int:
    assert int(num1) == num1 and int(num2) == num2, 'GCD is being calculated for Integers only!'
    if num1 < 0:
        num1 = -num1
    if num2 < 0:
        num2 = -num2
    if num2 == 0:
        return num1
    return gcd(num2, num1 % num2)
