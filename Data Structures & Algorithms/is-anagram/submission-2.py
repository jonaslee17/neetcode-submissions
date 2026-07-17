class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        mapS = {}
        for x in range(len(s)):
            if s[x] in mapS:
                mapS[s[x]] += 1
            else: mapS[s[x]] = 1
        for y in range(len(t)):
            if t[y] in mapS:
                mapS[t[y]] -= 1
                if mapS[t[y]] == 0:
                    mapS.pop(t[y])
            else: return False
        return True