class Solution:
    def minOperations(self, logs: List[str]) -> int:
        callStack = []

        for operation in logs:
            if operation == "../" or operation == './':
                if operation == "../" and len(callStack) != 0:
                    callStack.pop()
            else:
                callStack.append(operation)
        return len(callStack)
                