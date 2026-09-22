class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        maxArea = 0
        

        for i in range(len(heights)):
            startIndex = i

            while stack and heights[i] < stack[-1][1]:
                oldStart, oldHeight = stack.pop()

                currentArea = oldHeight * (i - oldStart)
                maxArea = max(currentArea, maxArea)

                startIndex = oldStart
            stack.append((startIndex, heights[i]))
        while stack:
            startIndex, height = stack.pop()
            currentArea = height * (len(heights) - startIndex)
            maxArea = max(currentArea, maxArea)
        
        return maxArea

        #also was unsure how to approach the startindex#




        