class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = R = 0 

        while L < len(nums) and R < len(nums):
            if nums[L] == 0 and nums[R] != 0 and R > L:
                nums[L], nums[R] = nums[R], nums[L]
                L+=1
                R+=1
            elif nums[L] != 0:
                L+=1
            else:
                R+=1