# Container With Most Water
# You are given an integer array heights where heights[i] 
# represents the height of the ith bar

# You may choose any two bars to form a container. Return 
# the maximum amount of water a container can store.

# Example 1:
# Input: height = [1,7,2,5,4,7,3,6]

# Output: 36
# Example 2:

# Input: height = [2,2,2]

# Output: 4
# Constraints:

# 2 <= height.length <= 1000
# 0 <= height[i] <= 1000

from typing import List

def maxArea(heights: List[int]) -> int:
    left, right = 0, len(heights) - 1
    max_water = 0

    while left < right:
        width = right - left
        max_water = max(max_water, min(heights[left], heights[right]) * width)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_water

height1 = [1, 7, 2, 5, 4, 7, 3, 6]
height2 = [2, 2, 2]
print(maxArea(height1))
