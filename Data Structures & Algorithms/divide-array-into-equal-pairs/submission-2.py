class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        frequencies = Counter(nums)

        for num, value in frequencies.items():
            if value % 2 != 0:
                return False
        return True