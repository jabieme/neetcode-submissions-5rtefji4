class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i=0
        while pow(2,i) <= n:
            if pow(2,i)== n:
                return True
            i+=1
        return False