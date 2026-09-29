class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        ans = i == len(s)    

        while i < len(s):
            i += 1

        while j < len(t):
            j += 1    

        return ans  
        