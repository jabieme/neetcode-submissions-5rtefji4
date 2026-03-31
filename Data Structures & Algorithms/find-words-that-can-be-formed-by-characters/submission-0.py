class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        for word in words:
            charCount = Counter(chars)
            wordCount = Counter(word)
            valid = True
            for c in word:
                if charCount[c] < wordCount[c]:
                    valid = False
            if valid:
                res+=len(word)
        
        return res