class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        #a + b + c = 0
        for i, a in enumerate(nums):
            if a > 0:
                break
            L = i+1
            R = len(nums)-1
            while L < R:
                b, c = nums[L], nums[R]
                threeSum = a + b + c
                if threeSum > 0:
                    R-=1
                elif threeSum < 0:
                    L+=1
                else:
                    if [a,b,c] not in res:
                        res.append([a, b, c])
                    L+=1
                    R-=1
        return(res)
