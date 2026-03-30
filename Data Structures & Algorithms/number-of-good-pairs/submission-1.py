class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        total = 0
        dicts = defaultdict(int)
        for num in nums:
            total += dicts[num]
            dicts[num]+=1
        return total