class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0

        while (left != right) :
            
            tempMax = (right - left) * min(heights[left], heights[right])

            if (tempMax > maxArea):
                maxArea = tempMax

            if heights[left] <= heights[right]:
                left += 1
                continue
            if heights[right] <= heights[left]:
                right -= 1
                continue
        
        return maxArea