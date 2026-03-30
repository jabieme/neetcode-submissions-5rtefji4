class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram1 = {}
        anagram2 = {}
      
        for char in s:
            if char in anagram1:
                anagram1[char] += 1
            else:
                anagram1[char] = 1
        for char in t:
            if char in anagram2:
                anagram2[char] += 1
            else:
                anagram2[char] = 1
        
        return anagram1 == anagram2
