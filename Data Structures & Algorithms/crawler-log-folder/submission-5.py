class Solution:
    def minOperations(self, logs: List[str]) -> int:
        callStack = []
        for operation in logs:
            if operation == '../':
                if callStack:
                    callStack.pop()
            elif operation != "./":
                callStack.append(operation)
        return len(callStack)