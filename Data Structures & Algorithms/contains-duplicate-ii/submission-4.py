class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in mp:
                if i - mp[num] <= k:
                    return True
            mp[num] = i
        return False