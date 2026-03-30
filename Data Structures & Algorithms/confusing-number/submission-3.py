class Solution:
    def confusingNumber(self, n: int) -> bool:
        confusingMap = {"0":"0", "1":"1", "6":"9", "8":"8","9":"6"}
        numStr = str(n)
        res=""
        for char in numStr:
            if char not in confusingMap:
                return False
            else:
                res+=confusingMap[char]
        if len(res)>1:
            numList = list(res)
            L, R = 0, len(numList)-1
            while L < R:
                numList[L], numList[R] = numList[R], numList[L]
                L+=1
                R-=1
            res = "".join(numList)
            print(res)
        return int(res)!=n