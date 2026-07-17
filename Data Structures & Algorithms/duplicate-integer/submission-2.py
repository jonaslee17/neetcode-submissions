class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repeat = set()
        for i in nums:
            if i in repeat:
                return True
            repeat.add(i)
        return False