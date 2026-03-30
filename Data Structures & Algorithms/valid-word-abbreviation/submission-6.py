class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        L = R = 0 
        m, n = len(word), len(abbr)

        while L < m and R < n:
            sublen=0
            if abbr[R] == '0':
                return False

            if word[L] == abbr[R]:
                L, R = L +1, R+ 1
            elif abbr[R].isalpha():
                return False
            else:
                while R < n and abbr[R].isdigit():
                    sublen = sublen * 10 + int(abbr[R])
                    R += 1
                L += sublen
        return L == m and R == n