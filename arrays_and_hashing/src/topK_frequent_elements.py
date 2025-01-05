# Given an integer array nums and an integer k, return the k 
# most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Example 1:

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]
# Example 2:

# Input: nums = [7,7], k = 1

# Output: [7]

from typing import List

# def topKFrequent(nums: List[int], k: int) -> List[int]:
#     results = {}

#     for num in nums:
#         if num not in results:
#             results[num] = 0
#         results[num] += 1

#     # top_K = []
#     # for _ in range(k):
#     #     max_key = max(results, key=results.get)
#     #     top_K.append(max_key)
#     #     del results[max_key]
#     # return top_K

#     results_sorted = dict(sorted(results.items()), key=lambda val: val[1])
#     top_K = list(results_sorted.keys())[:k]
#     return top_K

# Method 2 (O(n * log(k))), space complexity: o(n)
# import heapq
# from collections import Counter
# def topKFrequent(nums: List[int], k: int) -> List[int]:
#     counter = Counter(nums)
#     heap = []

#     for key, val in counter.items():
#         if len(heap) < k:
#             heapq.heappush(heap, (val, key))
#         else:
#             heapq.heappushpop(heap, (val, key))
#     return [h[1] for h in heap]

# Method: Bucket sort algorithm (O(n))
from collections import Counter
def topKFrequent(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    counter = Counter(nums)
    buckets = [0] * (n + 1) # to include the 0 frequency

    # Fill the buckets with values of the dictionaries as frequencies
    for num, freq in counter.items():
        if buckets[freq] == 0:
            buckets[freq] = [num]
        else:
            buckets[freq].append(num)
    
    # Return the top K elements
    top_K = []
    for i in range(n, -1, -1):
        if buckets[i] != 0:
            top_K.extend(buckets[i])
        if len(top_K) == k:
            break
    
    return top_K


# Solution:
# from collections import Counter
# def topKFrequent(nums: List[int], k: int) -> List[int]:
#     counter = Counter(nums)
#     top_k = counter.most_common(k) # heapq approach
#     print(top_k)
#     return list(map(lambda x: x[0], top_k))


    
# Neetcode
# class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     count = {}
    #     freq = [[] for i in range(len(nums) + 1)]

    #     for num in nums:
    #         count[num] = 1 + count.get(num, 0)
    #     for num, cnt in count.items():
    #         freq[cnt].append(num)
        
    #     res = []
    #     for i in range(len(freq) - 1, 0, -1):
    #         for num in freq[i]:
    #             res.append(num)
    #             if len(res) == k:
    #                 return res

nums = [1,2,2,3,3,3]
k = 2

# nums = [7,7]
# k = 1

# nums=[1,1,1,2,2,3]
# k=2

print(topKFrequent(nums, k))
