class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nonDupes = set()
        i = 0
        for num in nums:
            if num not in nonDupes:
                nonDupes.add(num)
                nums[i] = num
                i += 1
        return len(nonDupes)