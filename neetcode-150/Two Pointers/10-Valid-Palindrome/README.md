# 10 - Valid Palindrome

**Difficulty:** Easy | **Link:** https://neetcode.io/problems/is-palindrome/question?list=neetcode150

## 1. Problem Description
```text
Given a string s, return true if it is a palindrome, otherwise return false.
A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all
non-alphanumeric characters. Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).
```

**Example 1:**
```text
Input: s = "Was it a car or a cat I saw?"
Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.
```

**Example 2:**
```text
Input: s = "tab a cat"
Output: false
Explanation: "tabacat" is not a palindrome.
```
**Constraints:**
```text
1 <= s.length <= 1000
s is made up of only printable ASCII characters.
```

## 2. My Approach
```text
This is a simple two pointers problem. Since the question specifies that its case insensitive
and that your solution should ignore all non-alphanumeric characters, I first construct the
version of the string with only the alphanumeric chars. Then, I lower the entire string's case
to make it case insensitive. Then, I simply define a pointer at the start and end, incrementing
them inwards as converging pointers and performing a check for inequality between characters
during each iteration (returning false if any alternate pair of characters are inequal).
```
