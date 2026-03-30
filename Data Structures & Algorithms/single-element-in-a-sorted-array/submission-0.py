class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        maps = {}

        for num in nums:
            if num in maps:
                maps[num] += 1
            else:
                maps[num] = 1
        
        for key in maps.keys():
            if maps[key] == 1:
                return key
        