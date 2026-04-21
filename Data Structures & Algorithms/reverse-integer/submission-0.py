class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        numArr = list(str(x))
        L, R = 0, len(numArr)-1
       
        while L < R:
            if numArr[L] == "-":
                L+=1
                continue
            numArr[L], numArr[R] = numArr[R], numArr[L]
            L+=1
            R-=1
        complete = int("".join(numArr))

        if complete > int(math.pow(2,31)-1) or complete < -2**31:
            return 0
        return complete