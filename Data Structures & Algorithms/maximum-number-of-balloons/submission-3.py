class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = Counter(text)
        string = Counter("balloon")
        minAmount = float('inf')

        for letter, count in string.items():
           minAmount = min((freq[letter] // count),minAmount)
        return minAmount