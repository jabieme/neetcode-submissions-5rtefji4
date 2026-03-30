class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        m = len(s)
        L, R = 0, m-1

        while L < R:
            s[L], s[R] = s[R],s[L]
            L+=1
            R-=1

        start = 0
        for i in range(m):
            if i+1 >= m or s[i+1] == " ":
                end = i
                while start < end:
                    s[start], s[end] = s[end],s[start]
                    start+=1
                    end-=1
                start = i+2
        print(s)