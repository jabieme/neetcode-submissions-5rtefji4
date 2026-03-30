class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        shortestDistance = float("inf")
        word1Idx = float("inf")
        word2Idx = float("inf")
        for i in range(len(wordsDict)):
            word = wordsDict[i]
            if word == word1:
                word1Idx = i
            elif word == word2:
                word2Idx = i
            if len(wordsDict) > word1Idx and len(wordsDict) > word2Idx:
                shortestDistance = min(shortestDistance, abs(word1Idx - word2Idx))
        return shortestDistance
                