class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0

        while left < right:

            if heights[left] < heights[right]:
                current = heights[left] * (right - left)
                left += 1
            else:
                current = heights[right] * (right - left)
                right -= 1
            if current > maxArea:
                maxArea = current
        return maxArea
                
            