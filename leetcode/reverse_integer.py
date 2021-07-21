class Solution(object):
    def reverse(self, x):

        s = len(str(x)[::-1])
        if x>0 and int(str(x)[::-1]) < 2**31:
            return int(str(x)[::-1])                                # converting into int in order to take care of x = 120 case. After inversion it should be 21 and not 021.
        elif x<0 and s-1 != 0 and int(str(x)[::-1][:(s-1)])< 2**31:   # str(x)[::-1] => inversion, str(x)[::-1][:(s-1)] => substringing everything except last element(which will be '-' sign as x < 0)
            return (-1)*int(str(x)[::-1][:(s-1)])
        else:
            return 0

print(Solution().reverse(1534236469))
print(Solution().reverse(123))
print(Solution().reverse(-123))
print(Solution().reverse(120))
print(Solution().reverse(0))

# Runtime: 12 ms in Leetcode.