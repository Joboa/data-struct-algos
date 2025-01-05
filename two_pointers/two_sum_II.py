# Two Integer Sum II
# Given an array of integers numbers that is sorted in non-decreasing order.

# Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a 
# given target number target and index1 < index2. Note that index1 and index2 cannot be equal, 
# therefore you may not use the same element twice.

# There will always be exactly one valid solution.

# Your solution must use 
# O
# (
# 1
# )
# O(1) additional space.

# Example 1:

# Input: numbers = [1,2,3,4], target = 3

# Output: [1,2]
# Explanation:
# The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2.
# We return [1, 2].

from typing import List

# def twoSum(numbers: List[int], target: int) -> List[int]:
#     if not numbers:
#         return []
    
#     for i in range(len(numbers)):
#         diff = target - numbers[i]
#         if diff in numbers and numbers.index(diff) != i:
#             return [i + 1, numbers.index(diff) + 1]
#     return []

from collections import defaultdict

def twoSum(numbers: List[int], target: int) -> List[int]:
    prevMap = defaultdict(int)
    
    for i, n in enumerate(numbers):
        diff = target - numbers[i]
        if diff in prevMap:
            return [prevMap[diff] + 1, i + 1]
        prevMap[n] = i
    return []

# Neetcode
# Binary search
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         for i in range(len(numbers)):
#             l, r = i + 1, len(numbers) - 1
#             tmp = target - numbers[i]
#             while l <= r:
#                 mid = l + (r - l)//2
#                 if numbers[mid] == tmp:
#                     return [i + 1, mid + 1]
#                 elif numbers[mid] < tmp:
#                     l = mid + 1
#                 else:
#                     r = mid - 1
#         return []

# two pointers time: O(n), space O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []



numbers = [1,2,3,4]
target = 7
# numbers=[2,3,4]
# target=6
print(twoSum(numbers, target))