class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patternMap = {}
        sentenceArr = s.split(" ")
        wordHistory = set()
        if len(pattern)!= len(sentenceArr):
            return False
        for i in range(len(pattern)):
            character = pattern[i]
            word = sentenceArr[i]

            if character not in patternMap:
                if word in wordHistory:
                    return False
                patternMap[character] = word
                wordHistory.add(word)
            else:
                if patternMap[character]!=word:
                    return False
        return True