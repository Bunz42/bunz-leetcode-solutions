class Solution:
    def maxArea(self, heights: List[int]) -> int:
        j = 0
        k = len(heights) - 1
        max_area = min(heights[j], heights[k]) * (k - j)

        while j < k:
            if heights[j] < heights[k]:
                j += 1
            else:
                k -= 1
            
            curr_area = min(heights[j], heights[k]) * (k - j)
            if curr_area > max_area:
                max_area = curr_area
        
        return max_area
