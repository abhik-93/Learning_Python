# For binary, base = 2
# Say, num = 11
# To find: binary of 11
# Step 1: 11/2 = quotient 5 and remainder 1
# Step 2: 5/2 = quotient 2 and remainder 1
# Step 3: 2/2 = quotient 1 and remainder 0
# Step 4: 1/2 = quotient 0 and remainder 1
# So, stop when quotient = 0
# binary of 11 = 1011
# Logic Step 1: Divide the number by 2
# Logic Step 2: Get the integer quotient for the next iteration
# Logic Step 3: Get the remainder for the binary digit
# Logic Step 4: Repeat the steps until the quotient == 0


def decimal_to_binary(num: int) -> int:
    assert int(num) == num, 'Input number should be Integer only'
    quotient = int(num / 2)
    remainder = num % 2
    if quotient == 0:
        return remainder
    return remainder + decimal_to_binary(quotient) * 10
