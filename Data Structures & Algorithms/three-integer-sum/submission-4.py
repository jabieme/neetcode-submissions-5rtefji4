class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            L = i + 1
            R = len(nums)-1
            while L < R:
                b = nums[L]
                c = nums[R]
                threeSum = num + b + c
                if threeSum == 0:
                    if [num, b, c] not in res:
                        res.append([num, b, c])
                    R-=1
                    L+=1
                elif threeSum > 0:
                    R-=1
                else: 
                    L+=1
        return res
