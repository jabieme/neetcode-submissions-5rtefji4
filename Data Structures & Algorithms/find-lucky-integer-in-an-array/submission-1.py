class Solution:
    def findLucky(self, arr: List[int]) -> int:
        maxLucky = -1
        luckyFreq = Counter(arr)
        
        for num in set(arr):
            if num in luckyFreq and luckyFreq[num] == num:
                maxLucky = max(maxLucky, num)
        return maxLucky