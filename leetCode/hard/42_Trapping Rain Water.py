class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        rains = 0
        left = 0
        right = len(height) - 1

        left_max = height[left]
        right_max = height[right]

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max <= right_max:
                rains += left_max - height[left]
                left += 1
            else:
                rains += right_max - height[right]
                right -= 1

        return rains
