class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resultList = list()
        subMap = {}
        for i in range(len(nums)):
            if nums[i] in subMap:
                resultList.append(subMap[nums[i]])
                resultList.append(i)
                return resultList
            else:
                sum = target - nums[i]
                subMap[sum] = i
            
                