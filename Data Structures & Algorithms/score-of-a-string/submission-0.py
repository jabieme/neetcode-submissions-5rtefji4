class Solution:
    def scoreOfString(self, s: str) -> int:
        i = 0
        dif = 0
        while i < len(s) and i+1 < len(s):
            dif += abs(ord(s[i]) - ord(s[i+1]))
            i+=1
        return dif