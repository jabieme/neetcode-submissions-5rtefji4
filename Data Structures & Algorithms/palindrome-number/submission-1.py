class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        L=0
        R=len(num)-1
        while L < R:
            if num[L] != num[R]:
                return False
            L+=1
            R-=1
        return True