# You are given an array non-negative integers height which represent an 
# elevation map. Each value height[i] represents the height of a bar, 
# which has a width of 1.

# Return the maximum area of water that can be trapped between the bars.

# Input: height = [0,2,0,3,1,0,1,3,2,1]

# Output: 9

from typing import List

def trap(height: List[int]) -> int:
    if not height or len(height) < 3:
        return 0
    
    n = len(height)
    total_water = 0

    max_left = [0] * n
    max_right = [0] * n

    # Fill left array
    max_left[0] = height[0]
    for i in range(1, n):
        max_left[i] = max(height[i], max_left[i - 1])

    
    # Fill right array
    max_right[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        max_right[i] = max(height[i], max_right[i + 1])

    # Trapped water
    for i in range(n):
        filled_water = min(max_left[i], max_right[i]) - height[i]
        if filled_water > 0:
            total_water += filled_water

    return total_water


# Neetcode solutin on two pointers
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if not height:
#             return 0

#         l, r = 0, len(height) - 1
#         leftMax, rightMax = height[l], height[r]
#         res = 0
#         while l < r:
#             if leftMax < rightMax:
#                 l += 1
#                 leftMax = max(leftMax, height[l])
#                 res += leftMax - height[l]
#             else:
#                 r -= 1
#                 rightMax = max(rightMax, height[r])
#                 res += rightMax - height[r]
#         return res


height = [0,2,0,3,1,0,1,3,2,1]
print(trap(height))