class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                nums[j],previous = previous,nums[j]
                
        return nums
        
