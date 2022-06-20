class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s

        pattern = {_:"" for _ in range(numRows)}
        row = 0
        dir = -1

        for _ in s:
            pattern[row] += _
            if row == 0 or row == numRows - 1:      # When row = 0 and when row = num - 1, we should change the direction
                dir = -dir
            row += dir

        return "".join([r for r in pattern.values()])


print(Solution().convert("PAYPALISHIRING", 3))
print(Solution().convert("PAYPALISHIRING", 4))
print(Solution().convert("A", 1))

# Runtime: 40 ms in Leetcode