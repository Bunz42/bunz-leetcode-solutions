# 14 - Trapping Rain Water

**Difficulty:** Hard | **Link:** https://neetcode.io/problems/trapping-rain-water/question?list=neetcode150

## 1. Problem Description
```text
You are given an array of non-negative integers height which represent an elevation map.
Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.
```

**Example 1:**

<img width="798" height="318" alt="image" src="https://github.com/user-attachments/assets/b7b204b1-d73c-4ae2-a353-4bf504a5acbf" />

```text
Input: height = [0,2,0,3,1,0,1,3,2,1]
Output: 9
```

**Constraints:**
```text
1 <= height.length <= 1000
0 <= height[i] <= 1000
```

## 2. My Approach
```text
1. Need to find a way to determine the amount of water trapped at a specific position in the array.
	-> I think the way to do this is to find the greater elements to the left and right of the current position, then subtract the height at the current position from the minimum height surrounding it on either side.
	-> Thus, the formula is as follows: min(height[l], height[r]) - height[idx]

2. You could just brute force this problem by running an algorithm that repeatedly finds the greater elements to the left and right of the current position for every single index i, but that would be an inefficient solution,
because some of the positions have the same greater left and right elements as their adjacent positions. Therefore, this would involve redundant repetition.

3. So, a way to combat this could be to store the greater left and right elements in a separate array, then iterate through the intervals created in that array, keeping height[l] and height[r] the same across each index in
each distinct interval. However, there's an even better way with a two pointers approach.

4. The actual algorithm (two pointers approach):
	-> To trap water at a particular index, the area trapped is entirely limited by the shorter of the two highest walls on either side.
	-> So, if I put a pointer at the start and one at the end, I can keep track of the highest wall seen from both the left and right.
	-> Since the smaller of the two walls is the bottleneck, I just compare the two tallest walls and see which one is shorter, then calculate the area with the shorter one inconsideration. Then, I update my tallest left wall or
	tallest right wall accordingly.
	-> To calculate trapped water, just use something along the lines of trapped_water += shortest_of_the_two_walls - height[i]
```
