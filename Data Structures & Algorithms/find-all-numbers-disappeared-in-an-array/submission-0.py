class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        res=[]
        for i in range(1,len(nums)+1):
            if i not in nums:
                res.append(i)
        return res
