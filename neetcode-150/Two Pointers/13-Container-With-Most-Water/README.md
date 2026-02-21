# 13 - Container With Most Water

**Difficulty:** Medium | **Link:** https://neetcode.io/problems/max-water-container/question?list=neetcode150

## 1. Problem Description
```text
You are given an integer array heights where heights[i] represents the height of the ith bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.
```

**Example 1:**

<img width="789" height="485" alt="image" src="https://github.com/user-attachments/assets/a33117bc-7f42-4ad0-ab39-a00e63dcbf2d" />

```text
Input: height = [1,7,2,5,4,7,3,6]
Output: 36
```

**Example 2:**
```text
Input: height = [2,2,2]
Output: 4
```

**Constraints:**
```text
2 <= height.length <= 1000
0 <= height[i] <= 1000
```

## 2. My Approach
```text 
This is a pretty simple two pointers problem. Just initialize two pointers, one at each end of the array, then define a max_area variable to track the biggest area found so far. 
To calculate the area of water held, simply use the minimum between the two heights at the two pointers, and then multiply it by the width of the container (p2 - p1).
Repeat this process while the two pointers are valid (i.e. p1 < p2), and after each iteration, just increment the pointer associated with the shorter height (in an inwards fashion), because its the only way for
the area to get bigger anyway.
Every time a new area is a calculated, make it your new max_area if it's bigger than your previous max_area variable.
Return the max area at the end.
```
