class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L=len(nums)
        answer=[]
        for i in range(L):
            for j in range(i+1, L):
                if nums[i]+nums[j]==target:
                   answer.append(i)
                   answer.append(j) 
        return answer