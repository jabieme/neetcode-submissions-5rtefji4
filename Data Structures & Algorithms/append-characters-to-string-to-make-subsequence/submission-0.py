class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ptr = 0 

        for char in s:
            if ptr < len(t) and char == t[ptr]:
                ptr+=1
        return len(t)-ptr if ptr < len(t) else 0