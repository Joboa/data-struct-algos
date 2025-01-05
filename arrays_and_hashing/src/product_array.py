# Products of Array Except Self
# Given an integer array nums, return an array output where
# output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in
# O
# (
# n
# )
# O(n) time without using the division operation?

# Example 1:

# Input: nums = [1,2,4,6]

# Output: [48,24,12,8]
# Example 2:

# Input: nums = [-1,0,1,2,3]

# Output: [0,-6,0,0,0]

from typing import List
# def productExceptSelf(nums: List[int]) -> List[int]:
#     n = len(nums)
#     # res = []
#     res = [0] * n

#     for i in range(n):
#         prod = 1
#         for j in range(n):
#             if i == j:
#                 prod = prod * 1 # continue
#             else:
#                 prod = prod * nums[j]
#         # res.append(prod)
#         res[i] = prod
#     return res

# Method 2
# import copy
# def productExceptSelf(nums: List[int]) -> List[int]:
#     def prod_nums(arr):
#         prod = 1
#         for num in arr:
#             prod = prod * num
#         return prod

#     res = []
#     n = len(nums)

#     for i in range(n):
#         curr_nums = nums.copy()
#         curr_nums.pop(i)
#         res.append(prod_nums(curr_nums))

#     return res


def productExceptSelf(nums: List[int]) -> List[int]:
    res = [1] * len(nums)
    prefix_r = [1] * len(nums)
    postfix_r = [1] * len(nums)

    # Prefix iteration
    prefix = 1
    for i in range(len(nums)):
        prefix_r[i] = prefix
        prefix = prefix * nums[i]
    print(prefix_r)

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        postfix_r[i] = postfix
        postfix = postfix * nums[i]
    print(postfix_r)

    for i in range(len(nums)):
        res[i] = prefix_r[i]* postfix_r[i]
    return res

# def productExceptSelf(nums: List[int]) -> List[int]:
#     res = [0] * (len(nums))

#     prefix = 0
#     for i in range(len(nums)):
#         res[i] = prefix
#         prefix += nums[i]

#     postfix = 0
#     for i in range(len(nums) - 1, -1, -1):
#         res[i] += postfix
#         postfix += nums[i]
#     return res


# Neetcode:
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         res = [1] * (len(nums))

#         prefix = 1
#         for i in range(len(nums)):
#             res[i] = prefix
#             prefix *= nums[i]
#         postfix = 1
#         for i in range(len(nums) - 1, -1, -1):
#             res[i] *= postfix
#             postfix *= nums[i]
#         return res


nums = [1, 2, 4, 6]
# nums = [-1,0,1,2,3]
print(productExceptSelf(nums))
