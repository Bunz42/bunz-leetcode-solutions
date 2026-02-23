# 16 - Longest Substring Without Duplicates

**Difficulty:** Medium | **Link:** https://neetcode.io/problems/longest-substring-without-duplicates/question

## 1. Problem Description
```text
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.
```

**Example 1:**
```text
Input: s = "zxyzxyz"

Output: 3

Explanation: The string "xyz" is the longest without duplicate characters.
```

**Example 2:**
```text
Input: s = "xxxx"

Output: 1
```

**Constraints:**
```text
0 <= s.length <= 1000
s may consist of printable ASCII characters.
```

## 2. My Approach
```text
A brute force approach to this problem would just be to iterate through each character in the string
and check subsequent characters until a duplicate is found. Then, keep track of the max length of
a found valid substring, returning it at the end. However, this is inefficient with an O(n^2) time
complexity.

Instead, a better way is to use the sliding window algorithm. For this problem, a dynamically
sized window is required, since the length of the substring isn't known and is actually what 
we're trying to find.

Using sliding window, I can reduce the time complexity to O(n) because I no longer have to iterate
through any redundant substrings.

Implementation:
- Define the window with a left and right pointer.
- Define a set of characters to track current substring being observed by the window.
- Expand the window by incrementing the right pointer.
- If the right pointer finds an element that's already part of the set, a dupe is found.
- Increment the left pointer, removing its element from the set until there's no more dupes.
- Calculate the length of the substring with l - r + 1.
- Update the maximum substring length if the length value is greater than the current max.
- Repeat until the right pointer reaches the end of the string.
- Return the max substring length.
```


