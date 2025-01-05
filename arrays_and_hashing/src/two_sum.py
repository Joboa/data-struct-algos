# Two Sum
# Given an array of integers nums and an integer target, 
# return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of 
# indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Example 1:

# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

# Example 2:

# Example 2:

# Input: nums = [4,5,6], target = 10

# Output: [0,2]
# Example 3:

# Input: nums = [5,5], target = 10

# Output: [0,1]

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(1,len(nums)):
            if nums[i] + nums[j] == target  and i != j:
              return [i, j]
            
    # No combinations
    return []


# Solution 2
# def twoSum(nums, target):
#     for i, num in enumerate(nums):
#         print("i", i)
#         diff = target - num
#         print("diff", diff)
#         if diff in nums and nums.index(diff) != i: 
#             print("i", i)
#             return [i, nums.index(diff)]
#     return []

# Neetcode
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         prevMap = {}  # val -> index

#         for i, n in enumerate(nums):
#             diff = target - n
#             if diff in prevMap:
#                 return [prevMap[diff], i]
#             prevMap[n] = i

# 