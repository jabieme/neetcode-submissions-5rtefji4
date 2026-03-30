class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num

        while l <= r:
            mid = l+(r-l)//2
            sq = mid*mid
            if sq > num:
                r = mid - 1
            elif sq < num:
                l = mid + 1
            else:
                return True

        return False