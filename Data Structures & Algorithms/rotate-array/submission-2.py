class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k%=n
        

        def reverse(L: int, R: int):
            while L < R:
                nums[L], nums[R] = nums[R], nums[L]
                L, R = L + 1, R - 1
        reverse(0, n-1)
        print(nums)
        reverse(0, k-1)
        print(nums)
        reverse(k, n-1)