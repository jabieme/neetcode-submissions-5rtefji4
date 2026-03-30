class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0
        L = 0
        for R in range(len(nums)):
            if currSum < 0:
                currSum = 0
                L = R
            currSum += nums[R]
            if maxSum < currSum:
                maxSum = currSum
        return maxSum
        