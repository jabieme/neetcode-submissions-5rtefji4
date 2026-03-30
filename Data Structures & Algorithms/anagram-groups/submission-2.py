class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashedWords = defaultdict(list)
        for word in strs:
            alphaFreq = [0] * 26
            for c in word:
                alphaFreq[ord(c) - ord("a")] = alphaFreq[ord(c) - ord("a")] + 1
            hashedWords[tuple(alphaFreq)].append(word)
        return hashedWords.values()
