# 17 - Longest Repeating Character Replacement

**Difficulty:** Medium | **Link:** https://neetcode.io/problems/longest-repeating-substring-with-replacement/question

## 1. Problem Description
```text
You are given a string s consisting of only uppercase english characters and an integer k.
You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.
```

**Example 1:**
```text
Input: s = "XYYX", k = 2

Output: 4

Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.
```

**Example 2:**
```text
Input: s = "AAABABB", k = 1

Output: 5
```

**Constraints:**
```text
1 <= s.length <= 1000
0 <= k <= s.length
```

## 2. My Approach
```text
To do this problem, I'm going to use the dynamic sliding window approach, because this problem
requires finding the length of a substring under a certain condition, which is 
pretty obviously fit for the sliding window pattern. Since the length of the substring
is what we're actually trying to find, we can't use a fixed sliding window for this.

To start, we first need to define how exactly to obtain the longest substring you can
with repeated character replacements. Basically, what you want to do is always choose
to replace the characters with lower frequencies with the characters that appear
most frequently. This is pretty obvious when you think of the optimal scenario, which
is just replacing letters to make all the characters identical. To do that with the
least number of replacements, you clearly need to replace characters with the
char that occurs most frequently.

To achieve this, I need some way to keep track of the frequency of a given character
in the string. I can probably use a hash map for this, where I store the character 
and its frequency as a key, value pair.

After I track the frequencies, I can calculate the number of replacements using the
difference between the string's total length and the frequency of the most common 
character.

Brute force approach:
Consider all the possible substrings, use a hash map to count frequencies, then return
the max length of the substring with at most k replacements. However, this would be 
an O(n^2) solution because you'd be checking redundant elements.

Sliding Window approach:
A better way to do this problem would be to define a dynamically sized window representing 
a substring that I'm currently "viewing" through this window. During each iteration, run 
an algorithm that calculates the minimum number of replacements needed by the formula I 
defined previously, then just shrink the window if it exceeds k replacements.

Actual Implementation:
1. Define the window as the maximum length it could possibly be, which is just the length of
the string s. Make a left pointer at the beginning, then iterate through he string with a right
pointer to set up the dynamic window.
2. Algorithm for calculating minimum number of replacements then shrinking the window
accordingly:
	- Define a hashmap/dictionary(python) at the beginning of the function
	- Define a max_length and max_freq variable to track the max substring length
	and max character frequency
	- Use count[s[right]] = count.get(s[right], 0) + 1 to add to the frequency
	of any new characters that enter the window when right is expanding.
	- Update the max frequency variable if the new frequency is greater than
	whatever it already was
	- Check if the current window is invalid (if size of the window - max_freq is
	bigger than k)
	- If it is, just shrink it from the left, updating the frequency of whatever
	character just left the window, and incrementing the left pointer.
3. Update the max_length once the substring is valid, if the substring's length 
is a new maximum.
4. Return the max_length at the very end.
```
