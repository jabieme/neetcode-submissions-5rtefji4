class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        ctr = Counter(nums)

        if ctr[target] > len(nums)/2:
            return True
        return False