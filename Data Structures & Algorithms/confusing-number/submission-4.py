class Solution:
    def confusingNumber(self, n: int) -> bool:
        confusingMap = {"0":"0", "1":"1", "6":"9", "8":"8","9":"6"}
        numStr = str(n)
        res=[]
        for char in numStr:
            if char not in confusingMap:
                return False
            res.append(confusingMap[char])
        res = "".join(res)
        return int(res[::-1])!=n