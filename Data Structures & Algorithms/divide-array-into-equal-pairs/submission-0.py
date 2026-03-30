class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        frequencies = Counter(nums)

        for num in set(nums):
            if frequencies[num] % 2 != 0:
                return False
        return True