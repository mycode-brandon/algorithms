"""
Easy solution using a hashmap (dict). By obtaining the complement to each number in the list, we can make only
one pass of the list instead of nesting two for loops. If we input the complement into the dict, we can just
directly check if the next number in the list is in the dict. If so, return those two indices.
"""


def twoSum(nums: list[int], target: int) -> list[int]:
    hashmap = dict()
    for index, number in enumerate(nums):
        complement = target - number
        if number in hashmap:
            return [hashmap[number], index]
        else:
            hashmap[complement] = index


assert twoSum([2, 7, 11, 15], 9) == [0, 1]
