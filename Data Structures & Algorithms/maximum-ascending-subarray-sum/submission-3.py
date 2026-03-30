class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSubSum = 0
        curSum = 0
        prev = -1
        for i in range(len(nums)):
            if prev != -1 and prev >= nums[i]:
                maxSubSum = max(curSum, maxSubSum)
                curSum = 0
            prev = nums[i]
            curSum += prev
        return max(maxSubSum, curSum)