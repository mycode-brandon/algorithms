# Same as isAnagram, but we need to additionally group the anagrams together in sub lists with list of words as input
# Let's try using our ascii character mapping method

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    result = {}
    for word in strs:
        character_map = [0] * 26
        for character in word:
            character_map[ord(character) - ord('a')] += 1
        result[''.join(character_map)].append(word)
    return result.values()


groupAnagrams(["eat","tea","tan","ate","nat","bat"])

