class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = set()
        for num in nums:
            dupes.add(num)
        return len(dupes) != len(nums)