class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums)-1
 
        while L <= R:
            mid = L + ((R-L) // 2)
            guess = nums[mid]
            if guess < target:
                L = mid + 1
            elif guess > target:
                R = mid - 1
            else:
                return mid
        return -1