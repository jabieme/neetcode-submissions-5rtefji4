class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        firstMin = float("inf")
        secondMin = float("inf")

        for price in prices:
            if price < firstMin:
                firstMin, secondMin = price, firstMin
            elif price < secondMin:
                secondMin = min(price, secondMin)

        leftover = money - (firstMin + secondMin)
        return leftover if leftover >= 0 else money