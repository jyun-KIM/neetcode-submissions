class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for c in s:
            if c=='(' or c=='{' or c=='[': 
                stack.append(c)
                print(stack)
                continue
            if (c==')' or c=='}' or c==']') and len(stack)==0:
                return False
            if c==')' and len(stack)!=0:
                temp=stack.pop()
                if temp != '(': return False
            if c=='}' and len(stack)!=0:
                temp=stack.pop()
                if temp != '{': return False
            if c==']' and len(stack)!=0:
                temp=stack.pop()
                print(temp)
                if temp != '[': return False
        if len(stack)!=0: return False
        return True
        