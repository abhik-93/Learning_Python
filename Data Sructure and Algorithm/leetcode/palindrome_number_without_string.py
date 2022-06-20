class Solution(object):

    def convertInttoList(self, n):
        l = []
        while n != 0:
            l = [n % 10] + l
            n = n // 10
        return l

    def isPalindrome(self, x):
        if x <= 2**31 -1 and x>= -2**31:
            if x>0:
                x = Solution().convertInttoList(x)
                return x == x[::-1]
            elif x<0:
                return False # Since negative integer will never be a palindrome
            elif x == 0:
                return True

print(Solution().isPalindrome(121))
print(Solution().isPalindrome(-121))
print(Solution().isPalindrome(10))
print(Solution().isPalindrome(-101))
print(Solution().isPalindrome(0))

#Runtime: 76 ms in Leetcode