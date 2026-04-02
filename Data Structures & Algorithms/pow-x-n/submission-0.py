class Solution:
    def myPow(self, x: float, n: int) -> float:
        total = 1

        for _ in range(abs(n)):
            total *= x
        if n < 0:
            total = 1/total
        return total