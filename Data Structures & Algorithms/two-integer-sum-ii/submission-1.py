class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers)-1

        while L < R:
            if target > numbers[R]+numbers[L]:
                L += 1
            elif target < numbers[R]+numbers[L]:
                R -= 1
            else:
                return [L+1, R+1]