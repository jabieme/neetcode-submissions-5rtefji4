class Solution:
    def findLucky(self, arr: List[int]) -> int:
        maxLucky = -1
        luckyFreq = {}

        for num in arr:
            if num not in luckyFreq:
                luckyFreq[num] = 1
            else:
                luckyFreq[num]+=1
        
        for num in set(arr):
            if num in luckyFreq and luckyFreq[num] == num:
                maxLucky = max(maxLucky, num)
        return maxLucky