class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqMap = {}

        for i in range(len(nums)):
            if nums[i] not in freqMap:
                freqMap[nums[i]] = 1
            else:
                freqMap[nums[i]] += 1
        print(freqMap)
        for item in freqMap.items():
            if freqMap[item[0]] >= len(nums) // 2:
                return item[0]
        return 0