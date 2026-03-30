class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freq = Counter(nums)
        maxNum = -1

        for num in nums:
            if freq[num] == 1:
                maxNum = max(maxNum, num)
        return maxNum