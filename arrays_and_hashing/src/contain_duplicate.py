"""
Contains Duplicate
Given an integer array nums, return true if any value appears more than 
once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
"""
from typing import List


def hasDuplicate(nums: List[int]) -> bool:
    nums.sort()
    return True if list(set(nums)) != nums else False

# Time complexity: O(nlog(n))

# Neetcode solution
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         return len(set(nums)) < len(nums)

# Time complexity: O(n)


# if __name__ == "__main__":
#     # nums = [1, 2, 3, 3]
#     # nums = [1, 2, 3, 4]
#     nums = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -
#             11, -12, -13, -14, -15, -16, -17, -18, -19, -20]
    # print(sorted(nums))
    # print(sorted(list(set(nums))))
    # print(hasDuplicate(nums))
