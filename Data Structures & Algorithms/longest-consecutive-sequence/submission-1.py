class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        count = 0
        longest = 0
        
        for i in nums:
            if i not in seen:
                seen.add(i)
        
        for i in nums:
            if i - 1 not in seen:
                curSeq = []
                curSeq.append(i)
                while i+1 in seen:
                    curSeq.append(i+1)
                    i += 1
                count = len(curSeq)

                print("curseq list:", curSeq)
                print("curseq length:", len(curSeq))
                print("count:", count)
                longest = max(longest, count)
        return longest
