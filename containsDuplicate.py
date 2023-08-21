# Extremely simple method that doesn't use sorting, but uses memory O(n) instead
# Time: O(n) Space: O(n)

def containsDuplicate(nums: list[int]) -> bool:
    test = set()
    for i in nums:
        if i in test:
            return True
        test.add(i)
    return False


assert containsDuplicate([1, 2, 3, 4, 5]) == False
assert containsDuplicate([1, 2, 3, 4, 4]) == True
