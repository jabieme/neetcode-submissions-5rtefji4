class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sGram=Counter(s)
        tGram=Counter(t)

        for char, count in sGram.items():
            if len(sGram) != len(tGram):
                return False
            if char not in tGram:
                return False
            if tGram[char] != count:
                return False
        return True
        