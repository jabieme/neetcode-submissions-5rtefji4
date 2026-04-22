class Solution:
    def maxScore(self, s: str) -> int:
        counts = Counter(s)
        numOfZeros = 0
        numOfOnes = 0
        maxNum = float("-inf")

        for i in range(len(s)-1):
            if s[i] == "0":
                numOfZeros += 1
            else:
                numOfOnes +=1
            maxNum = max(numOfZeros + (counts["1"]-numOfOnes),maxNum)
        return maxNum