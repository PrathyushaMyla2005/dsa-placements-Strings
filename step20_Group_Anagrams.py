'''group anagrams together
example: input: ["eat", "tea", "tan", "ate", "nat", "bat"]
output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
'''
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):

        # Create hashmap
        anagram_map = defaultdict(list)

        # Traverse each word
        for word in strs:

            # Sort the word
            sorted_word = ''.join(sorted(word))

            # Add original word to hashmap
            anagram_map[sorted_word].append(word)

        # Return grouped anagrams
        return list(anagram_map.values())
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution = Solution()
print(solution.groupAnagrams(strs)) #output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
'''tc o(n * k log k) where n is the number of strings and k is the maximum length of a string, because we sort each string which takes o(k log k) time, sc o(n * k) because in the worst case we may have to store all strings in the hashmap'''
