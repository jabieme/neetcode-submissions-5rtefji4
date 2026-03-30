class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        i=-1
        while not words[i]:
            i-=1
        return len(words[i])