class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        numSet = set(nums)
        res=[]
        for i in range(1,len(nums)+1):
            if i not in numSet:
                res.append(i)
        return res
