class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #Option 1: go through each possible are value, store that into a separate list, and then extract the largest value in from list
            # Complexity: Space = O(n), Time = O(n)
        
        #Ask interviewer the complexity they would like to see
        # Suppose they ask for Space = O(1), Time = O(n)
        #We can't create previous algorithm b/c it uses extra space than what is asked

        #Option 2: create two pointers left and right, with left representing the leftmost index and right representing the rightmost index
        # Left can represent the height while right will be used to track the distance between left and right (basically the width)
        # create an integer to update the value of 

        left = 0
        right = len(heights) - 1
        maxA = 0

        while (left < right):
            height = min(heights[left], heights[right])
            width = right - left
            area = height*width
            if (area > maxA):
                maxA = area
            if (heights[left] < heights[right]):
                left += 1
            else:
                right -= 1
        return maxA






#ex -> [1,7,2,5,4,7,3,6], left = 0, right = 7
#   height = min(1, 6) = 1
#   dist between left and right = right - left = 7
#   area = 1 * 7 = 7 = maxA
#   
#   height = min(7,6) = 6
#   dist between left and right = 7 - 6 = 36, max A = 