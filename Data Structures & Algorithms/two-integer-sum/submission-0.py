class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for x in range(len(nums)):
            if target - nums[x] in hashmap:
                return [hashmap[target - nums[x]], x]
            hashmap[nums[x]] = x
        return