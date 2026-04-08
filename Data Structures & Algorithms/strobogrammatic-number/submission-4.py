class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        stroboNums = {
            "0":"0",
            "1":'1',
            "6":"9",
            "8":"8",
            "9":"6"
        }
        res=""
        for i in range(len(num)-1, -1, -1):
            if num[i] not in stroboNums:
                return False
            else:
                res += stroboNums[num[i]]
        print(res)
        return res==num