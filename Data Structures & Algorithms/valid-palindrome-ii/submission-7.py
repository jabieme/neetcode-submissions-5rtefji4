class Solution:
    def validPalindrome(self, s: str) -> bool:
        delete = 0
        L, R = 0, len(s)-1
        if len(s) == 2 and s[L] != s[R]:
            return True

        while L <= R:
            if delete > 1:
                return False
            elif s[L] == s[R]:
                L+=1
                R-=1
            else:
                if s[R-1] == s[L]:
                    R-=1
                elif s[L+1] == s[R]:
                    L+=1
                else:
                    print("L: " +  s[L])
                    print("R: " + s[R])
                    return False
                delete+=1
                
        return True
            
        