class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        trapped_water = 0

        tallest_left = height[l]
        tallest_right = height[r]

        while l < r:
            if tallest_left < tallest_right:
                l += 1
                tallest_left = max(tallest_left, height[l])
                trapped_water += tallest_left - height[l]
            
            else:
                r -= 1
                tallest_right = max(tallest_right, height[r])
                trapped_water += tallest_right - height[r]
        
        return trapped_water
