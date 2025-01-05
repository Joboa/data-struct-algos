# Valid Anagram
# Given two strings s and t, return true if the two strings are anagrams of each other,
# otherwise return false.

# An anagram is a string that contains the exact same characters as another string,
# but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true
# Example 2:

# Input: s = "jar", t = "jam"

# Output: false
# Constraints:

# s and t consist of lowercase English letters.

# My solution 1
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    def character_count(c: str):
        char_dict = {}
        for char in c:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

        return char_dict
     
    s_dict = character_count(s)
    t_dict = character_count(t)

    return s_dict == t_dict

# Solution 2
# def isAnagram(s: str, t: str) -> bool:
#     from collections import Counter

#     return Counter(s) == Counter(t)

# Neetcode
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
            
#         return sorted(s) == sorted(t)

if __name__ == "__main__":
    s = "racecar"
    t = "carrace"
    isAnagram(s, t)
