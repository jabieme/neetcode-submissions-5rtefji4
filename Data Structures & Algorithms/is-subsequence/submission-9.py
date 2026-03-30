class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        L = R = 0

        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False

        while R < len(t):
            if L < len(s) and s[L] == t[R]:
                L+=1
                R+=1
            else:
                R+=1
       
        return R == len(t) and L == len(s)