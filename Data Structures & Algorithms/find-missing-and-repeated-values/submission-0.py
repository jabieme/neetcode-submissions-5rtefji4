class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        numSet = set()
        res = []
        n=0
        for arr in grid:
            n+=len(arr)
            for num in arr:
                if num in numSet:
                    res.append(num)
                numSet.add(num)
        print(n)
        for i in range(1,n+1):
            if i not in numSet:
                res.append(i)
        return res