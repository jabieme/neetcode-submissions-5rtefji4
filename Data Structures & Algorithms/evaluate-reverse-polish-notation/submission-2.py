class Solution:
    def is_integer(self,character: str):
        try:
            int(character)
            return True
        except ValueError:
            return False
    def evalRPN(self, tokens: List[str]) -> int:
        mathStack = []
        for character in tokens:
            if self.is_integer(character):
                mathStack.append(character)
            else:
                if mathStack:
                    num2 = int(mathStack.pop())
                    num1 = int(mathStack.pop())
                    match character:
                        case "+":
                            sums=num1+num2
                            mathStack.append(str(sums))
                        case "-":
                            difference=num1-num2
                            mathStack.append(str(difference))
                        case '*':
                            product=num1*num2
                            mathStack.append(str(product))
                        case "/":
                            quotient=num1/num2
                            mathStack.append(str(math.trunc(quotient)))
        return int(mathStack[0])