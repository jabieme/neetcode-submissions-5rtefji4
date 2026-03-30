class Solution:
    def maxDifference(self, s: str) -> int:
        freqs={}
        for character in s:
            if character in freqs:
                freqs[character]+=1
            else:
                freqs[character]=1
        maxOdd = -float('inf')
        minEven = float('inf')
        for val in freqs.values():
            if val % 2 == 1:
                maxOdd = max(val, maxOdd)
            else:
                minEven = min(val, minEven)
        return int(maxOdd - minEven)