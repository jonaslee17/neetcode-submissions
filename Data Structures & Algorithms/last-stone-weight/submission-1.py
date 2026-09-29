class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-value for value in stones]
        heapq.heapify(stones)        
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x < y:
                heapq.heappush(stones,x-y)
            elif y > x:
                heapq.heappush(stones,y-x)
            else:
                continue
        return -(stones[0]) if stones else 0