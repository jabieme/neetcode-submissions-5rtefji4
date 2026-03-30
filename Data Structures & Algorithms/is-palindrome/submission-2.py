class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        L, R = 0, len(s)-1
        while L < R:
            left, right = s[L], s[R]
            if left.isalnum() and right.isalnum():
                if left != right:
                    return False
                else:
                    L+=1
                    R-=1
            elif not left.isalnum():
                L+=1
            else:
                R-=1
        return True