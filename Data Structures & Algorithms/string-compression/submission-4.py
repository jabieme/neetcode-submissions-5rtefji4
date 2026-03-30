class Solution:
    def compress(self, chars: List[str]) -> int:
        L = R = 0
        count=0
        res = ""
        while L < len(chars) or R <= len(chars):
            if R != len(chars) and chars[L] == chars[R]:
                count+=1
            else:
                res += chars[L]
                if count > 1:
                    res += str(count)
                    count =1
                L=R
            R+=1

        for i, char in enumerate(res):
            chars[i] = char
        return len(res)
