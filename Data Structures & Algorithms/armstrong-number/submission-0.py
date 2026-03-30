class Solution:
    def isArmstrong(self, n: int) -> bool:
        k = len(str(n))
        total = 0
        temp_num = n
        while temp_num > 0:
            hold = temp_num % 10
            total += math.pow(hold, k)
            temp_num //= 10
        
        return total == n