class Solution:
    def countCharacters(self, word:str)->Dict[str, int]:
        return tuple(sorted(list(word)))
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Hash Frequency Fingerprint
        #Find the characters frequency hashmap. 
        freqHashTable = {}
        for word in strs:
            freqHash = self.countCharacters(word)
            if freqHash in freqHashTable:
                freqHashTable[freqHash].append(word)
            else:
                freqHashTable[freqHash]=[word]
        return list(freqHashTable.values())