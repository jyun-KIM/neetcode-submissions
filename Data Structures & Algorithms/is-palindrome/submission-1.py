class Solution:
    def isPalindrome(self, s: str) -> bool:
        L=0
        R=len(s)-1
        while L<=R:
            while not ((ord('A')<=ord(s[L])<=ord('Z')) or (ord('a')<=ord(s[L])<=ord('z')) or (ord('0')<=ord(s[L])<=ord('9'))):
                L+=1
            while not ((ord('A')<=ord(s[R])<=ord('Z')) or (ord('a')<=ord(s[R])<=ord('z')) or (ord('0')<=ord(s[R])<=ord('9'))):
                R-=1
            if s[L].lower()!=s[R].lower(): 
                return False
            L+=1
            R-=1
            print(L,R)
        return True
        