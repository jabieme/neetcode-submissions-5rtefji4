class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for operation in logs:
            if operation == "../" or operation == "./":
                if stack and operation == "../": 
                    stack.pop()
            else:
                stack.append(operation)

        return len(stack)