class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i, num in enumerate(nums):
            if num == 0:
                for j, num2 in enumerate(nums[i + 1:]):
                    if num2 != 0:
                        nums[i], nums[i + 1 + j] = nums[i + 1 + j], nums[i]
                        break
                