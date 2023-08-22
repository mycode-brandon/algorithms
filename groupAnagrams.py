# Same as isAnagram, but we need to additionally group the anagrams together in sub lists with list of words as input
# Let's try using our ascii character mapping method

# currently not working because if there are greater than 9 elements the digit rolls from 9 to 10, which doesn't convert well to string value
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    result = {}
    for word in strs:
        character_map = [0] * 26
        for character in word:
            character_map[ord(character) - ord('a')] += 1
        key = ''.join([str(i) for i in character_map])
        print("key: ", key, "word: ", word, "length of key: ", len(key))
        if key in result:
            result[key].append(word)
        else:
            result[key] = [word]
    return list(result.values())


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams(["bdddddddddd","bbbbbbbbbbc"]))

