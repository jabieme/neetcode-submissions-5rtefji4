class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        for move in shift:
            if move[0] == 0:
                s = s[move[1]:]+s[:move[1]]
            else:
                s = s[-move[1]:]+s[:-move[1]]
        return s