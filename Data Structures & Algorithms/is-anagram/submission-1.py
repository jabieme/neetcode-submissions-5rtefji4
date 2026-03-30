class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charCount = {}
        charCount2 = {}
        for i in range(len(s)):
            if s[i] in charCount:
                charCount[s[i]] = charCount[s[i]] + 1
            else:
                charCount[s[i]] = 1

            if t[i] in charCount2:
                charCount2[t[i]] = charCount2[t[i]] + 1
            else:
                charCount2[t[i]] = 1

        return charCount == charCount2
                

        
        