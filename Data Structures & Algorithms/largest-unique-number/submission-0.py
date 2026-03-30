class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freq = {}
        maxNum = -1

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        for num in nums:
            if freq[num] == 1:
                maxNum = max(maxNum, num)
        return maxNum