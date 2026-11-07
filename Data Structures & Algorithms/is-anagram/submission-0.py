class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s,t 길이 다르면 탈락
        if len(s)!=len(t): return False
        # s,t hashmap 선언
        countS, countT = {}, {}
        # 하나씩 돌면서 개수 세기
        for i in range(len(s)):
            countS[s[i]] = 1+countS.get(s[i],0)
            countT[t[i]] = 1+countT.get(t[i],0)
        # 다른 값 있으면 false
        for j in countS:
            if countT.get(j,0)!=countS[j]: return False

        return True