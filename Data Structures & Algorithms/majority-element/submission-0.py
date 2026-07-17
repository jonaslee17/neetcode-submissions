class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        result, maxCount = 0,0
        for num in nums:
            count[num] = 1+ count.get(num, 0)
            result = num if count[num]>maxCount else result
            maxCount = max(count[num], maxCount)
        return result
