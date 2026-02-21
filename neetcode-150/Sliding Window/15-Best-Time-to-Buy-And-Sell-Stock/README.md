# 15 - Best Time to Buy And Sell Stock

**Difficulty:** Easy | **Link:** https://neetcode.io/problems/buy-and-sell-crypto/question

## 1. Problem Description
```text
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
```

**Example 1:**
```text
Input: prices = [10,1,5,6,7,1]

Output: 6

Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.
```

**Example 2:**
```text
Input: prices = [10,8,7,5,2]

Output: 0

Explanation: No profitable transactions can be made, thus the max profit is 0.
```

**Constraints:**
```text
1 <= prices.length <= 100
0 <= prices[i] <= 100
```

## 2. My Approach
```text
For this problem, a brute force approach would be to just iterate through each price and evaluate the profit with each subsequent price, 
tracking the maximum profit. However, this approach is really slow with an O(n^2) time complexity.

Instead, I can solve this problem with the sliding window pattern to reduce to O(n). 
To solve this problem, I'm going to need a dynamically sized window, which I can define with
a left and right pointer, with the left pointer being the day I buy, and the right being the day I sell.

All there is to this problem is finding the lowest possible day to buy, then finding the highest price
after it to calculate the profit with. If you think about it, the only way for the profit to ever increase
is if there's another lower buy day after the one you just calculated the profit with. That's why
I only need to recalculate the profit if I actually find a lower buy day.

Actual implementation:
- Initialize two pointers, left (initial buy day) at 0 and right at 1. This is our initial window of size 2.
- Also, initialize a variable to track max profit.
- Increment the right pointer as long as its still in the array
- If the price at the left pointer is lower than the price at the right pointer,
calculate the profit of the current window and update the max profit if its a new maximum
- If the price at the left pointer is ever greater than the right pointer,
move the window so that it starts at the right pointer (left = right) and start calculating
profits using that new dynamic window.
- Always increment the right pointer by 1.
- Return the max profit at the end.
```
