class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {}
        return self.recur(n, cache)
    def recur(self, n:int, cache):
        if n in cache:
            return cache[n]
        if n <= 2:
            return 1 if n != 0 else 0
        result = self.recur(n-1,cache)+self.recur(n-2,cache)+self.recur(n-3,cache)
        cache[n] = result
        return result