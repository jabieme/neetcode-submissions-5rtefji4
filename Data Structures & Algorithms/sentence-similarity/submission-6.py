class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        similarWordsMap = {}
        if len(sentence1)!=len(sentence2):
            return False
       
        for i in range(len(sentence1)):
            j=0
            while j < len(similarPairs):
                if sentence1[i] in set(similarPairs[j]):
                    similarWordsMap[sentence1[i]] = set(similarPairs[j])
                if sentence2[i] in set(similarPairs[j]):
                    similarWordsMap[sentence2[i]] = set(similarPairs[j])
                j+=1
        
        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i]:
                return True
            if sentence1[i] not in similarWordsMap or sentence2[i] not in similarWordsMap:
                return False
            if sentence1[i] not in similarWordsMap[sentence1[i]] or sentence2[i] not in similarWordsMap[sentence1[i]]:
                if sentence1[i] not in similarWordsMap[sentence2[i]] or sentence2[i] not in similarWordsMap[sentence2[i]]:
                    return False 
        return True
        

