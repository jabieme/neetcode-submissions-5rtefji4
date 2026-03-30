class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashedWords = {}
        for word in strs:
            alphaFreq = [0] * 26
            for c in word:
                alphaFreq[ord(c) - ord("a")] = alphaFreq[ord(c) - ord("a")] + 1
            if tuple(alphaFreq) in hashedWords:
                hashedWords[tuple(alphaFreq)].append(word)
            else:
                newResultList = list()
                newResultList.append(word)
                hashedWords[tuple(alphaFreq)] = newResultList
        return hashedWords.values()




            
        