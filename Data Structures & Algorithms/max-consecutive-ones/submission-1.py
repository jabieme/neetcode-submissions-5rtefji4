class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxNum = 0
        count = 0
        for num in nums:
            if num == 1:
                count +=1
            else:
                count = 0
            maxNum = max(count, maxNum)
     
        return maxNum