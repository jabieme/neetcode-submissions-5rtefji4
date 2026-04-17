class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        maxNum = -1
        nums.sort()
        left, right = 0, len(nums)-1

        while left < right:
            sumOfNums = nums[left]+nums[right]
            if sumOfNums < k:
                maxNum = max(sumOfNums, maxNum)
                left+=1
            else:
                right-=1
            
        return maxNum