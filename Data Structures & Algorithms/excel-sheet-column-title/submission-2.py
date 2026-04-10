class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        columnPairs = {}

        for i in range(len(alphabet)):
            columnPairs[i+1]=alphabet[i]
        
        res=""
        while columnNumber > 0:
            columnNumber -= 1
            res = columnPairs[(columnNumber % 26) + 1] + res
            columnNumber //= 26
        return res