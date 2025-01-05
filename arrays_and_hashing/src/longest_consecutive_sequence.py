# Longest Consecutive Sequence
# Given an array of integers nums, return the length of the longest
# consecutive sequence of elements that can be formed.

# A consecutive sequence is a sequence of elements in which each
# element is exactly 1 greater than the previous element. The
# elements do not have to be consecutive in the original array.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [2,20,4,10,3,4,5]

# Output: 4
# Explanation: The longest consecutive sequence is [2, 3, 4, 5].

# Example 2:

# Input: nums = [0,3,2,5,4,6,1,1]

# Output: 7
# Constraints:

# 0 <= nums.length <= 1000
# -10^9 <= nums[i] <= 10^9

from typing import List

# def longestConsecutive(nums: List[int]) -> int:
#     c = sorted(set(nums))
#     cons_seq = []

#     for i in range(len(c) - 1):
#         if c[i + 1] - c[i] == 1:
#             if c[i] not in cons_seq:
#                 cons_seq.append(c[i])
#             cons_seq.append(c[i + 1])

#     return len(cons_seq)

def longestConsecutive(nums: List[int]) -> int:
    if not nums:
        return 0

    nums = sorted(set(nums))
    longest_cons = 1
    current_cons = 1

    for i in range(len(nums) - 1):
        if nums[i + 1] - nums[i] == 1:
            current_cons += 1
        else:
            longest_cons = max(longest_cons, current_cons)
            current_cons = 1

    return max(longest_cons, current_cons)


# nums = [2,20,4,10,3,4,5]
nums = [0, 3, 2,5,4,6,1,1]
print(longestConsecutive(nums))
