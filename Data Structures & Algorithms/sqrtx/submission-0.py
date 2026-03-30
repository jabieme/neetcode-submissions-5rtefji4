class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        res = 0
        while l <= r:
            mid = l + (r-l) // 2
            sq = mid * mid
            print(mid)
            if sq > x:
                r = mid - 1
            elif sq < x:
                l = mid + 1
                res = mid
            else:
                return mid
        return res