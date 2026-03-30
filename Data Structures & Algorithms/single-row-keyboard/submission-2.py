class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        charIdx = {}

        for i in range(len(keyboard)):
            charIdx[keyboard[i]] = i
        total = 0 
        prev=0
        for char in word:
            total += abs(charIdx[char] - prev)
            prev=charIdx[char]
        return total
            