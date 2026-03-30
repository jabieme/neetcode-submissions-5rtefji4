class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wordList = s.split(" ")
        print(wordList)
        i = -1
        while wordList[i] == "":
            i-=1
        return len(wordList[i])