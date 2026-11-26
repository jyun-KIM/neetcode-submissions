class Solution:
    def isAlpha(self, c)->bool:
        if ord('A')<=ord(c)<=ord('Z') or ord('a')<=ord(c)<=ord('z'):
            return True
    def isNum(self, c:str)->bool:
        if ord('0')<=ord(c)<=ord('9'):
            return True

    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<r and 0<=l and r<=len(s):
            while not (self.isAlpha(s[l]) or self.isNum(s[l])): l+=1
            while not (self.isAlpha(s[r]) or self.isNum(s[r])): r-=1
            if self.isAlpha(s[l]) and self.isAlpha(s[r]):
                if s[l].lower() != s[r].lower(): return False
            elif self.inNum(s[l]) and self.inNum(r):
                if s[l]!=s[r]: return False
            else: return False
            l+=1
            r-=1
        return True

        