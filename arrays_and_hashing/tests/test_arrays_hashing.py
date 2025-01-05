import pytest
from src.contain_duplicate import hasDuplicate
from src.valid_anagram import isAnagram
from src.two_sum import twoSum
from src.group_anagrams import groupAnagrams


@pytest.mark.parametrize("nums, expected",[
    ([1, 2, 3, 3], True),
    ([1, 2, 3, 4], False),
    ([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -
            11, -12, -13, -14, -15, -16, -17, -18, -19, -20], False)
])
def test_contain_duplicate(nums, expected):
    assert hasDuplicate(nums) == expected

@pytest.mark.parametrize("s, t, expected",[
    ("racecar", "carrace", True),
    ("jar", "jam", False)])
def test_valid_anagram(s, t, expected):
    assert isAnagram(s, t) == expected


@pytest.mark.parametrize("nums, target, expected",[
    ([3,4,5,6], 7, [0, 1]),
    ([4,5,6], 10,  [0, 2]),
    ([5, 5], 10, [0, 1])])
def test_two_sum(nums, target, expected):
    assert twoSum(nums, target) == expected

inp1 = ["act","pots","tops","cat","stop","hat"]
out1 =  [["hat"],["act", "cat"],["stop", "pots", "tops"]]
inp2 = ["x"]
out2 =  [["x"]]
inp3 = [""]
out3 =  [[""]]
@pytest.mark.parametrize("strs, expected",[
    # (inp1, out1),
    (inp2, out2),
    (inp3, out3)])
def test_group_anagrams(strs, expected):
    assert groupAnagrams(strs) == expected