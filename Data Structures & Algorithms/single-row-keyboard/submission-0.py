class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        charIdx = {}
        stack = []
        for i in range(len(keyboard)):
            charIdx[keyboard[i]] = i
        total = 0 
        for char in word:
                if stack and charIdx[char] == stack[-1]:
                    continue
                if stack and stack[-1]:
                    print('happened1')
                    total += abs(charIdx[char] - stack.pop())
                else:
                    print("happened2")
                    total +=charIdx[char]
                stack.append(charIdx[char])
        return total
            