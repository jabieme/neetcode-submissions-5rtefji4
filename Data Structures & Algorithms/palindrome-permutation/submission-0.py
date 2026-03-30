class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        hashmap = Counter(s)
        odds = sum(val % 2 for val in hashmap.values())
        return odds <=1