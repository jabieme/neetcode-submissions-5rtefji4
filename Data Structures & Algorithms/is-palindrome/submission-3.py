class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        print(s)
        L,R = 0, len(s)-1
        
        while(L<R):
            if s[L].isalnum() and s[R].isalnum():
                if s[L]!=s[R]:
                    return False
                L+=1
                R-=1
            elif not s[L].isalnum():
                L+=1
            else:
                R-=1
        return True