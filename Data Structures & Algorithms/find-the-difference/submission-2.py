class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sCount = Counter(s)
        tCount = Counter(t)

        for c in t:
            if c not in sCount:
                return c
            if sCount[c] != tCount[c]:
                return c
                