class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checknums = set(nums)
        if len(nums) == len(checknums):
            return False
        return True
        
