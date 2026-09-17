class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       sums = {}
       for i, num in enumerate(nums):
            dif = target - num
            if dif in sums:
                return [sums[dif], i]
            sums[num] = i
            