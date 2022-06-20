class Solution(object):
    def twoSum(self, nums, target):
        d={}
        for i,num in enumerate(nums):
            if target-num in d:             # Checking if difference of tarrget and actual number present in the list is present in the dictionary. Initially it will not be present, hence will be added in the code d[num] = i
                 return [d[target-num],i]
            d[num]=i
        return []

if __name__=='__main__':
    print(Solution().twoSum([2,7,11,15], 9))
    print(Solution().twoSum([3,2,4], 6))
    print(Solution().twoSum([3,3], 6))

# Runtime: 27 ms in Leetcode