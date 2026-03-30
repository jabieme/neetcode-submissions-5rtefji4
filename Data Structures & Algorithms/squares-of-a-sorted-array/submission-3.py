class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        L, R = 0, len(nums)-1
        
        while L <= R:
            sqrtL = nums[L] * nums[L]
            sqrtR = nums[R] * nums[R]
            
            if sqrtL > sqrtR:
                res.append(sqrtL)
                L+=1
            else:
                res.append(sqrtR)
                R-=1
          
        return res[::-1]
