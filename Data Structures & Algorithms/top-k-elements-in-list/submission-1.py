class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[] for i in range(len(nums)+1)]
        result=[]
        for num in nums:
            count[num]=count.get(num,0)+1
        for key,v in count.items():
            freq[v].append(key)

        for i in range(len(nums),0,-1):
            for n in freq[i]:
                result.append(n)
                if len(result)==k: return result



        