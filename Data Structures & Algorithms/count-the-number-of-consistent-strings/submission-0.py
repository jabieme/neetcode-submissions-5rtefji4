class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        length=0
        for word in words:
            valid = True
            for letter in word:
                if letter not in allowed:
                    valid = False
            if valid:
                length+=1
        return length