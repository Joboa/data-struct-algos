# Group Anagrams
# Given an array of strings strs, group all anagrams together into sublists. 
# You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, 
# but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]
# Example 3:

# Input: strs = [""]

# Output: [[""]]

from typing import List


# solution 1
def groupAnagrams(strs: List[str]) -> List[List[str]]:

    # Edge case 1: if the strs is empty ("")
    empty_list = list()
    empty_list.append("")
    if strs == empty_list:
        return [strs]
    

    # Edge case 2: if the strs contain only one character
    if len(strs) == 1:
        return [strs]

    words_dict = {}
    for i, word in enumerate(strs):
        word_s = "".join(sorted(word))
        if word_s in words_dict:
            words_dict[word_s].append(strs[i])
        else:
            words_dict[word_s] = [strs[i]]

    return list(words_dict.values())


# solution 2
# def groupAnagrams(strs: List[str]) -> List[List[str]]:
#     from collections import defaultdict
#     # Edge case 1: if the strs is empty ("")
#     empty_list = list()
#     empty_list.append("")
#     if strs == empty_list:
#         return [strs]
    

#     # Edge case 2: if the strs contain only one character
#     if len(strs) == 1:
#         return [strs]

#     words_dict = defaultdict(list)
#     for word in strs:
#         word_s = "".join(sorted(word))
#         words_dict[word_s].append(word)

#     return list(words_dict.values())


# Neetcode:
# from collections import defaultdict

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = defaultdict(list)
#         for s in strs:
#             count = [0] * 26
#             for c in s:
#                 count[ord(c) - ord('a')] += 1
#             res[tuple(count)].append(s)
#         return list(res.values())