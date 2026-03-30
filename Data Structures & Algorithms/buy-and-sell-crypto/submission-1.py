class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        for i in range(len(prices)):
            maxPrice = 0
            j=i+1
            while j < len(prices):
                summ = prices[j]-prices[i] 
                maxPrice = max(maxPrice, summ)
                j+=1
            prices[i] = maxPrice
        print(prices)
        return max(prices)
        
