class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = {}
        for i, num in enumerate(nums):
            dif = target - num
            if dif in sum:
                return [sum[dif], i]
            sum[num] = i