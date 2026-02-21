# 11 - Two Sum II Input Array Is Sorted

**Difficulty:** Medium | **Link:** https://neetcode.io/problems/two-integer-sum-ii/question?list=neetcode150

## 1. Problem Description
> Given an array of integers numbers that is sorted in non-decreasing order.
> Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same > element twice.
> There will always be exactly one valid solution.
> Your solution must use O(1) additional space.

**Example 1:**
```text
Input: numbers = [1,2,3,4], target = 3
Output: [1,2]
Explanation: The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].
```

**Constraints:**
```text
2 <= numbers.length <= 1000
-1000 <= numbers[i] <= 1000
-1000 <= target <= 1000
```

## 2. My Approach
> Two pointers, one at the end and one at the beginning (since arr is sorted, pointer at the end will always be the greatest element and the pointer at the start will be the smallest)
> check the sum between the two values, and if it's greater than the target, decrement the right pointer, if it's less than the target, increment the left.
