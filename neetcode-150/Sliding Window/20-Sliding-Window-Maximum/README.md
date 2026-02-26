# 20 - Sliding Window Maximum

**Difficulty:** Hard | **Link:** https://neetcode.io/problems/sliding-window-maximum/question

## 1. Problem Description
```text
You are given an array of integers nums and an integer k. There is a sliding window of size k that
starts at the left edge of the array. The window slides one position to the right until it reaches
the right edge of the array.

Return a list that contains the maximum element in the window at each step.
```

**Example 1:**
```text
Input: nums = [1,2,1,0,4,2,6], k = 3

Output: [2,2,4,4,6]

Explanation:
Window position            Max
---------------           -----
[1  2  1] 0  4  2  6        2
 1 [2  1  0] 4  2  6        2
 1  2 [1  0  4] 2  6        4
 1  2  1 [0  4  2] 6        4
 1  2  1  0 [4  2  6]       6
```

**Constraints:**
```text
1 <= nums.length <= 100,000
-10,000 <= nums[i] <= 10,000
1 <= k <= nums.length
```

## 2. My Approach
```text
This problem is clearly a sliding window problem. It's literally called "Sliding Window Maximum".
In this problem, the window is specified to be a fixed size k. The window starts at the very
left of the array of integers, and slides one position to the right until it reaches the end.

The problem wants you to construct an array of the max element in the window during every 
iteration. A possible way to do this is by iterating through the window at each step, and
finding the maximum value within the window, adding it to the array. However, this solution
is pretty slow with a time complexity of O(n*k)

Instead, we need a way to dynamically update the maximum value found as the window slides along
the array. I'm going to need to use some data structure to store the values in each window that 
will allow me to find the maximum value in a window with a really fast time complexity.

There is actually a very appropriate data structure to use here, which allows for max value lookup
in O(1) linear time. We can use a heap. Specifically, a max heap.

What is a max heap?
Since we're doing a problem viewing it from a sliding window perspective, some people might not
know what a max heap is. So, I'm going to explain it briefly. Basically, you can think of a max-heap 
like a binary tree (a tree where each parent node only has 2 child nodes) that's complete. What I mean
by "complete" is that every level of the tree is going to be completely filled out except the last
level. This is because the whole point of the max heap is to just fill it with nodes that decrease
in value as you go from left->right, top->bottom with the root node being the max value so you can 
access it easily. Thus, there's not going to be any gaps within levels, with the exception of the 
last level if you don't have enough elements to fill it.

Because the levels are going to be filled, you can probably intuit that now the tree is basically
just the same thing as a 1D array, where the array indices can be mapped to the associated nodes in
the tree. Here's the mapping for that (if you want to know more, I'll make a guide on heaps sometime):
Left Child Node: 2 * index + 1
Right Child Node: 2 * i + 2
Parent Node: (i - 1) // 2

For this problem, I'm going to be handling the values in each window iteration with a heap. However,
you can't just use a regular max-heap for this question, because the values in the window are
going to change, meaning you have to remove values from the max-heap accordingly. Standard max-heaps are
only efficient at removing the root node (the max value) for extraction, so we're going to have to think of
a faster solution.

You can avoid deleting elements in the heap for this problem by just simply not deleting them! The reason
you can do this is because the only time I even care about deleting an integer from the heap is if it's
trying to trick me into thinking its the maximum of the current window, when its not even in the window.
So, you just pop the root max value whenever it exits the window.

To accomplish this, we can store not just single numbers in the heap, but value-index pairs instead.
Now, this is what the logic is going to look like:
1. Push the new (value, index) pair into the heap when it enters from the right of the window
2. Look at the root (max value) and check if its less than or equal to the current index - k.
If it is, then the max value got left behind outside the window.
If not, the value is valid and in the window right now.
3. If the root is valid, store it in our output array.

Heaps can push elements with O(logn) time complexity. So, the overall time complexity would be O(nlogn)

Actual implementation in python:
1. Python has a heapq structure already, so I'm going to use that since this problem's point is to learn
about sliding window, not about heaps. However it's a min-heap by default so I need to multiply the values 
by -1 to simulate a max heap.
2. Initialize the heap with k value-index pairs for the intial window.
3. Append the max of the first window with result.append(-heap[0][0])
4. Slide the window using a for loop
5. Push elements into the heap entering from the right
6. Pop the root whenever its not in the window anymore
7. Append the max value of the current window
8. Return the result array

ALTERNATE SOLUTION:
There's actually an even faster solution that I didn't think of. You can use a monotonic queue instead of
a heap/priority queue.

The reason you can do this is because if your window is moving to the right you actually dont care about the
elements aside from the newer and larger element, because that's the element that's going to live longest in the
queue for this specific problem. So, you can actually just use a monotonically decreasing queue where everytime 
a new number enters the window, it kicks out all the smaller numbers in front of it.

This allows us to use a deque() structure which allows for O(1) pop operations, thus reducing the time
complexity from O(nlogn) from the heap solution, to O(n).

Algorithm:
1. While the deque still has elements and the new element entering is greater than the elements at the back of the
deque, pop from the back.
2. Push the new element to the back of the deque
3. Check the front of the deque and if its index is no longer inside the window, just pop it from the front
4. Once your window is valid, the max is always going to be at the front of the queue, so just extract it.
```

