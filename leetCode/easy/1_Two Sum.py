class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            tmp = nums[i]
            for j in range(i + 1, len(nums)):
                if tmp + nums[j] == target:
                    return [i, j]
