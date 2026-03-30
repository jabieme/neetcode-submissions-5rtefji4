class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetIndex = []
        pastSum = {}
        for i in range(len(nums)):
            num = nums[i]
            if target - num in pastSum:
                targetIndex.append(pastSum[target-num])
                targetIndex.append(i)
                return targetIndex
            else:
                pastSum[num] = i
               
            
        return targetIndex