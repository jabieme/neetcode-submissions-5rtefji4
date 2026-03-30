class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        maxLen = 0
        for i in range(len(s)):
            currLen = 0
            seenLetter = set()
            start = i
            while start < len(s) and s[start] not in seenLetter:
                if s[start] in seenLetter:
                    seenLetter.remove(s[start])
                seenLetter.add(s[start])
                currLen = start-i
                maxLen = max(currLen, maxLen)
                start+=1
        return maxLen+1 if len(s)!=0 else 0