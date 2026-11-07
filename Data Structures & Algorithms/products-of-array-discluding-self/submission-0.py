class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[1]*n
        postfix=[1]*n
        result=[]
        i=1
        for num in range(n-1):
            prefix[i]=prefix[i-1]*nums[num]
            i+=1
        for j in range(n-1,0,-1):
            postfix[j-1]=postfix[j]*nums[j]
        for k in range(n):
            result.append(prefix[k]*postfix[k])
        return result

        