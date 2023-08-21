# The first method I think of is the brute force method. First, take a set of each string. Then zip that string with 0's
# to create a hashmap with values of 0 for each letter. Loop through length of both strings and then compare maps.
# Seems to be heavy on the memory assignments.
# Beats only 28% of users in Memory, but 83% in Runtime

# def isAnagram(s: str, t: str) -> bool:
#     length = len(s)
#     if length != len(t):
#         return False
#     set_s = set(s)
#     set_t = set(t)
#     map_s = dict(zip(set_s, [0]*length))
#     map_t = dict(zip(set_t, [0]*length))
#     for i in range(length):
#         map_s[s[i]] += 1
#         map_t[t[i]] += 1
#     return map_s == map_t

# Another method I found online was to basically do the same thing but without the dicts, sets, & zips
# Instead, a list of ALL letters is created and the indexes referenced by subtracting the ASCII value of 'a'
# Simpler, but less intuitive immediately
# Ended up using only slightly less memory and actually had greater runtime. Must be some optimization with inbuilt
# set and dict methods, and it did have to loop through each string

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    map_s = [0] * 26
    map_t = [0] * 26  # each index represents letters a-z. index 0 = 'a', index 25 = 'z', etc...
    for letter in s:
        map_s[ord(letter) - ord('a')] += 1
    for letter in t:
        map_t[ord(letter) - ord('a')] += 1
    return map_s == map_t

assert isAnagram("hello", "goodbye") == False
assert isAnagram("hello", "goodb") == False
assert isAnagram("bdoog", "goodb") == True
assert isAnagram("hello", "olleh") == True
assert isAnagram("hello", "goodb") == False
