class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        if not t: return False
          
        i = 0
        for c in t:
            try:
                if s[i] == c:
                    i += 1
            except IndexError:
                return True
        
        return True if i == len(s) else False
