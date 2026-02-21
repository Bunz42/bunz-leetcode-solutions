# 12 - 3Sum

**Difficulty:** Medium | **Link:** https://neetcode.io/problems/three-integer-sum/question?list=neetcode150

## 1. Problem Description
```text
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
```

**Example 1:**
```text
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
```

**Example 2:**
```text
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
```

**Example 3:**
```text
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```

**Constraints:**
```text
3 <= nums.length <= 1000
-10^5 <= nums[i] <= 10^5
```

## 2. My Approach
```text
Approach for the algo to find triplets:
- I need to try to think of a two pointers approach.
- Notice that you can rearrange the formula n1 + n2 + n3 = 0 to kind of follow an eqn similar to the classic Two Sum problem: n1 = -(n2 + n3) or -n1 = n2 + n3.
- Now, we just run the soln to two sum using a standard two pointers approach, an O(n) soln, on each element in the array, making the final soln O(n^2). This is what we're aiming for, 
because the brute force approach would be to check every triplet which is O(n^3).
- This means, I need to sort the array so I'm going to use python's list.sort().


Consider the constraint that you should not return any duplicate triplets:
- Now, I know the algorithm is going to be something using -nums[i] = nums[j] + nums[k] (with two pointers representing
j and k), so now I need to find a way to calculate indices j and k without dupes.
- Well, since the array is sorted, we know that any duplicate values will be right next to each other, and the only way we get duplicate pairs of j and k are if, after moving the pointers,
both j and k still point to the same values that they previously pointed to.
- Thus, the algorithm for skipping dupes will be as follows:
	- After finding a match, add it to the result, then increment j and decrement k once.
	- Then, write a loop that keeps incrementing j if the value its currently pointing to is the same value as it was one increment ago.
	- Do the same thing for k (but considering k is decrementing instead of incrementing).
	- Also, perform a check on i as well to achieve the same thing.
- This will ensure that no duplicate triplets are considered.
```
