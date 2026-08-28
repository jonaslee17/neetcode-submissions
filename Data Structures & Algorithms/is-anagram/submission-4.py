class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_hash = {}
        for i, j in enumerate(s):
            s_hash[j] = s_hash.get(j,0) + 1
        
        for i in t:
            s_hash[i] = s_hash.get(i,0) - 1

        for val in s_hash.values():
            if val != 0:
                return False
    
        return True