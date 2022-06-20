"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]


Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true



"""

######## Code #########

class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) >= 3:
            left_arr = arr[:arr.index(max(arr))]
            right_arr = arr[arr.index(max(arr)):]
            if left_arr == sorted(left_arr) and right_arr == sorted(right_arr, reverse = True) and len(left_arr + right_arr) == len(arr) and len(set(right_arr)) == len(right_arr) and len(set(left_arr)) == len(left_arr) and len(right_arr) > 1 and len(left_arr) > 0:
                return True
            else:
                return False
            
        else:
            return False
          
#### Runtime: 156 ms, faster than 99.15% of Python online submissions for Valid Mountain Array.
