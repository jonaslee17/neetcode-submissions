class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums)- 1 
        while lower <= upper:
            middle = (lower+upper)//2
            if nums[middle] == target:
                return middle
            elif target > nums[middle]:
                lower = middle + 1
            else:
                upper = middle - 1
        return -1

