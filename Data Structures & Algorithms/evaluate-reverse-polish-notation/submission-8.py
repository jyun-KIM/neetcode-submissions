class Solution:
    def isnum(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        #tokens 돌면서
        for t in tokens:
        #숫자면 stack에 append 
            if self.isnum(t): stack.append(float(t))
        #아니면 위에 2개 뽑아서 연산
            else:
                num1=stack.pop()
                if len(stack)!=0:
                    num2=stack.pop()
            #+,-,*,/ 조건문으로 계산. 숫자는 다시 stack.append()
                if t=='+': stack.append(num1+num2)
                if t=='-': stack.append(num2-num1)
                if t=='*': 
                    print(num1*num2)
                    stack.append(num1*num2)
                if t=='/': 
                    print(num2//num1)
                    stack.append(num2//num1)
        return (int(stack.pop()))
            

        