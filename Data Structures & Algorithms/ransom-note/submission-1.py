class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomFrequency = {}
        magazineFrequency = {}

        for character in ransomNote:
            if character not in ransomFrequency:
                ransomFrequency[character]=1
            else:
                ransomFrequency[character]+=1
        for character in magazine:
            if character not in magazineFrequency:
                magazineFrequency[character]=1
            else:
                magazineFrequency[character]+=1
        
        for item in ransomFrequency.items():
            if item[0] in magazineFrequency:
                if magazineFrequency[item[0]] < item[1]:
                    return False
            else:
                return False
        return True