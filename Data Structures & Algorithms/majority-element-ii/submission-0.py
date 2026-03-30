class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ctr = Counter(nums)
        res = []
        n = len(nums)
        for num, count in ctr.items():
            if count > n//3:
                res.append(num)
        return res