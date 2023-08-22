# Same as isAnagram, but we need to additionally group the anagrams together in sub lists with list of words as input
# Let's try using our ascii character mapping method

# This method only works if we convert the list to a tuple so it can be hashed and used as a key for the dictionary
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    result = {}
    for word in strs:
        character_map = [0] * 26
        for character in word:
            character_map[ord(character) - ord('a')] += 1
        key = tuple(character_map)
        # print("key: ", key, "word: ", word)
        if key in result:
            result[key].append(word)
        else:
            result[key] = [word]
    return list(result.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams(["bdddddddddd","bbbbbbbbbbc"]))
