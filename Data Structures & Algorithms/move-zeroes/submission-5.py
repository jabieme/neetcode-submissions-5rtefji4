class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L, R = 0, 0

        while L < len(nums) and R < len(nums):
            if nums[R]:
                tmp = nums[L]
                nums[L] = nums[R]
                nums[R] = tmp
                L += 1
                R += 1
            else:
                R+=1
            
        