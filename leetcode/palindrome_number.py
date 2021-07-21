class Solution(object):
    def isPalindrome(self, x):
        
        if x <= 2**31 -1 and x>= -2**31:
            x = str(x)
            return x == x[::-1]

print(Solution().isPalindrome(121))
print(Solution().isPalindrome(-121))
print(Solution().isPalindrome(10))
print(Solution().isPalindrome(-101))

#Runtime: 44ms in Leetcode