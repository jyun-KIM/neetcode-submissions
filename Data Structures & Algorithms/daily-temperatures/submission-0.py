class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        stack=[]
        output=[0]*l
        stack.append((0,temperatures[0]))
        for i in range(1,l-1):
            if len(stack)==0:
                stack.append((i,temperatures[i]))
            else:
                for j in range(len(stack)):
                    temp=stack.pop()
                    if temperatures[i]>temp[1]:
                        output[temp[0]]=i-temp[0]
                    else: stack.append(temp)
                stack.append((i,temperatures[i]))
        return output
        