class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq_map = {}
        for word in words:
            for c in word:
                if c not in freq_map:
                    freq_map[c]=1
                else:
                    freq_map[c]+=1
        n = len(words)
        for letter in freq_map:
            if freq_map[letter] % n != 0:
                return False
        return True