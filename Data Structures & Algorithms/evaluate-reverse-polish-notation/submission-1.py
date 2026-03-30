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
            print("current token:",character)
            if self.is_integer(character):
                mathStack.append(character)
            else:
                if mathStack:
                    print(mathStack)
                    num2 = int(mathStack.pop())
                    num1 = int(mathStack.pop())
                    match character:
                        case "+":
                            sums=num1+num2
                            print(num1,"+",num2,"=",sums)
                            print(sums,"added to mathStack")
                            mathStack.append(str(sums))
                        case "-":
                            difference=num1-num2
                            print(num1,'-',num2,'=',difference)
                            print(difference,'added to mathStack')
                            mathStack.append(str(difference))
                        case '*':
                            product=num1*num2
                            print(num1,'*',num2,'=',product)
                            print(product, 'added to mathStack')
                            mathStack.append(str(product))
                        case "/":
                            quotient=num1/num2
                            print(num1,'/',num2,'=',quotient)
                            print(quotient,'added to mathStack')
                            mathStack.append(str(math.trunc(quotient)))
        return int(mathStack[0])