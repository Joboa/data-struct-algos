# Encode and Decode Strings
# Design an algorithm to encode a list of strings to a single string.
# The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]
# Example 2:

# Input: ["we","say",":","yes"]

# Output: ["we","say",":","yes"]

from typing import List


# def encode(strs: List[str]) -> str:
#     # Empty array
#     if not strs:
#         return "|"

#     if len(strs) == 1 and strs[0] == "":
#         return "||"
#     return "/".join(strs)


# def decode(s: str) -> List[str]:
#     # Empty array
#     if s == "|":
#         return []
#     if s == "||":
#         return [""]

#     print("str: ", s)
#     return s.split("/")

# Neetcode
def encode(strs: List[str]) -> str:
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res


def decode(self, s: str) -> List[str]:
    res = []
    i = 0

    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1
        length = int(s[i:j])
        i = j + 1
        j = i + length
        res.append(s[i:j])
        i = j

    return res 


strs = ["neet", "code", "love", "you"]
# strs = ["we","say",":","yes"]
# strs = [""]
en = encode(strs)
print("encode: ", en)
# de = decode(en)
# print(de)
