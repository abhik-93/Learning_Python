# Referred https://www.educative.io/edpresso/longest-palindromic-substring-in-on-with-manachers-algorithm

class Solution:
    def modifiedStr(self, string):
        newString = ['#']
        for char in string:
            newString += [char, '#']
        return ''.join(newString)

    def longestPalindrome(self, s: str) -> str:
        s = Solution().modifiedStr(s)
        LPS = [0 for _ in range(len(s))]
        C = 0
        R = 0

        for i in range(len(s)):
            iMirror = 2*C - i
            if R > i:
                LPS[i] = min(R-i, LPS[iMirror])
            else:
                LPS[i] = 0
            try:
                while s[i + 1 + LPS[i]] == s[i - 1 - LPS[i]]:
                    LPS[i] += 1
            except:
                pass
            
            if i + LPS[i] > R:
                C = i
                R = i + LPS[i]
        
        r, c = max(LPS), LPS.index(max(LPS))
        return (s[c - r : c + r].replace("#",""))

print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("cbbd"))
print(Solution().longestPalindrome("a"))
print(Solution().longestPalindrome("ac"))

# Runtime: 140 ms in Leetcode