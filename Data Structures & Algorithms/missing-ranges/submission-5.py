class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        R=0
        res = []
        if len(nums)==0:
            res.append([lower,upper])
            return res
        if nums[0] != lower:
            res.append([lower, nums[0]-1])
       
        
        for L in range(len(nums)):
            R = L + 1

            if nums[L]==upper:
                break
            if R >= len(nums):
                res.append([nums[L]+1, upper])
            elif nums[R]-1 != nums[L]:
                res.append([nums[L]+1, nums[R]-1])
        return res


