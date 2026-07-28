class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rep = set()
        l = 0
        maxCount = 0
        for r in range(len(s)):
            while s[r] in rep:
                rep.remove(s[l])
                l +=1
            maxCount = max(maxCount, r - l +1)
            rep.add(s[r])
            
        return maxCount
