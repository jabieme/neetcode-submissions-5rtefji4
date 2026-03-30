class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wordList = s.split(" ")
        i = len(wordList)-1
        while wordList[i] == "":
            i-=1
        return len(wordList[i])