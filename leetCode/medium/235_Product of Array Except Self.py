class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []    # answer
        p = 1
        for i in range(len(nums)):  # first, from left to right
            out.append(p)
            p = p * nums[i]

        p = 1
        for i in range(len(nums) - 1, -1, -1):  # from right to left
            out[i] = out[i] * p
            p = p * nums[i]

        return out
