class Solution(object):
    def myAtoi(self, s):
 
        s = s.strip() # removing whitespaces
        neg = False
        res = 0
        
        if s and s[0] == '-':
            neg = True
        if s and (s[0] == '+' or s[0] == '-'):
            s = s[1:]
        if not s:
            return 0
        
        for _ in s:
            if _.isdigit():
                res = res * 10 + int(_)
            else:
                break
            
        if neg:
            res = -res
        
        res = max(min(res, 2**31-1), -2**31)
        return res


print(Solution().myAtoi("42"))
print(Solution().myAtoi("   -42"))
print(Solution().myAtoi("4193 with words"))
print(Solution().myAtoi("words and 987"))
print(Solution().myAtoi("-91283472332"))

# Runtime: 12ms in Leetcode