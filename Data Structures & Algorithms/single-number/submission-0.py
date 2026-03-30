class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashset = Counter(nums)
        for num in nums:
            if hashset[num] == 1:
                return num