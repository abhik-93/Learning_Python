class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = {}
        start = 0
        long = 0

        for idx, ch in enumerate(s):
            if ch in last and last[ch] >= start:
                start = last[ch] + 1
            else:
                long = max(long, idx - start + 1)

            last[ch] = idx
            
        return long

if __name__=='__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("bbbbb"))
    print(Solution().lengthOfLongestSubstring("pwwkew"))
    print(Solution().lengthOfLongestSubstring(""))

# Runtime: 32 ms in Leetcode