# top k frequent elements of a list of numbers.

# using bucket sort, this can be done in O(n) magnitude of time

# bucket sort:
# rather than going through and using the number as the key and the frequency of each element as the value
# which takes O(nlog(n)) time, bucket sort uses the frequency as the key and the number as the value, which
# only takes O(2n) time, which reduces to O(n) magnitude.

def topKFrequent(nums: [list[int]], k: int) -> list[int]:
    count = [[] for _ in range(len(nums)+1)]
    num_map = {}
    for number in nums:
        if number in num_map:
            num_map[number] += 1
        else:
            num_map[number] = 1
    for number, frequency in num_map.items():
        count[frequency].append(number)
    result = []
    for i in count[::-1]:
        for j in i:
            result.append(j)
        if len(result) == k:
            break
    return result

# only beats 10% of users in Python3 for Memory. There might be some optimization for my variable assignments.


print(topKFrequent([1, 2, 3, 4, 5, 5, 3, 2, 2, 2, 2], 3))
print(topKFrequent([1, 1, 1, 2, 2, 3], 2))

