class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i]=1+count.get(i,0)
        sorted_count = sorted(count.keys(), key= lambda num: count[num], reverse=True)
        return sorted_count[:k]