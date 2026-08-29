class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       count = {}
       maxCount = 0
       maxIndex = 0
       for i in nums:
            count[i] = count.get(i,0) + 1
            if count[i] > maxCount:
                maxIndex = i
            else:
                maxIndex
            maxCount = max(count[i], maxCount)
 
       return maxIndex