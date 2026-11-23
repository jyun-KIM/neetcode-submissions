class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        output=[0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<t:
                j=stack.pop()
                output[j]=i-j
            stack.append(i)
        return output
        