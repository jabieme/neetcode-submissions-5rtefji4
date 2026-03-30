class Logger:

    def __init__(self):
        self.logger = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        log = self.logger

        if message in log:
            if log[message] <= timestamp:
                log[message]=timestamp+10
                return True
            return False
        else:
            log[message] = timestamp+10
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
