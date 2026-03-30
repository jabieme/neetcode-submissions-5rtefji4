class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        largest = len(nums)
        
        for i in range(largest):
            if nums[i] != i:
                return i
        return len(nums)