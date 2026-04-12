class Solution:
    def maxScore(self, s: str) -> int:
        d = Counter(s[0:1])
        print(d)
        maxNum = float("-inf")
        for i in range(len(s) - 1):
            count1 = Counter(s[0:i+1])
            count2 = Counter(s[i+1:len(s)])
            print(count1)
            print(count2)
            print(count1['0']+count2['1'])
            maxNum = max(count1['0']+count2['1'], maxNum)
        return maxNum