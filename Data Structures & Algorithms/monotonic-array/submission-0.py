class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        sortArr = []
        if nums[0]<=nums[1]:
            sortArr = sorted(nums)
            print(sortArr)
        else:
            sortArr = sorted(nums,reverse=True)
        return sortArr == nums
