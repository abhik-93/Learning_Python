class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        res = nums1 + nums2         # appending two lists
        res = sorted(res)           # sorting res list and storing it in res
        mid = len(res) // 2         # finding the middle of length of res
        median = (res[mid] + res[~mid]) / 2     # finding the median
        return median


# Runtime: 68 ms in Leetcode