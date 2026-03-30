class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        numSet = set(nums)
        largest = len(nums)
        
        for i in range(0, largest+1):
            if i not in numSet:
                return i