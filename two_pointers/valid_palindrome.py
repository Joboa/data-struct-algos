# Valid Palindrome
# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward.
# It is also case-insensitive and ignores all non-alphanumeric characters.

# Example 1:

# Input: s = "Was it a car or a cat I saw?"

# Output: true
# Explanation: After considering only alphanumerical characters we have
# "wasitacaroracatisaw", which is a palindrome.

# Example 2:

# Input: s = "tab a cat"

# Output: false
# Explanation: "tabacat" is not a palindrome.

# Constraints:

# 1 <= s.length <= 1000
# s is made up of only printable ASCII characters.

from typing import List

# def isPalindrome(s: str) -> bool:
#     if not s:
#         return s

#     s = "".join(filter(str.isalnum, s)).lower()
#     print(s)

#     return s == s[::-1]

# Neetcode
def isPalindrome(s: str) -> bool:
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not str.isalnum(s[l]):
            l += 1
        while r > l and not str.isalnum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l, r = l + 1, r - 1
    return True


# def alphaNum(self, c):
#     return (ord('A') <= ord(c) <= ord('Z') or
#             ord('a') <= ord(c) <= ord('z') or
#             ord('0') <= ord(c) <= ord('9'))


if __name__ == "__main__":
    s = "Was it a car or a cat I saw?"
    # s = "tab a cat"
    print(isPalindrome(s))
