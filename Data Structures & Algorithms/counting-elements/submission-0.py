class Solution:
    def countElements(self, arr: List[int]) -> int:
        numsSet = set(arr)
        count = 0

        for num in arr:
            if num+1 in numsSet:
                count+=1
        return count