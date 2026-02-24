# 18 - Permutations in String

**Difficulty:** Medium | **Link:** https://neetcode.io/problems/permutation-string/question

## 1. Problem Description
```text
You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise.
That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.
```

**Example 1:**
```text
Input: s1 = "abc", s2 = "lecabee"

Output: true

Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".
```

**Example 2:**
```text
Input: s1 = "abc", s2 = "lecaabee"

Output: false
```

**Constraints:**
```text
1 <= s1.length, s2.length <= 1000
```

## 2. My Approach
```text
If I were to brute force this problem, i would sort s1, then sort every possible substring in
s2 and compare each sorted substring with the sorted s1. If any of them match, then I can
return true. However, checking every single substring is an O(n^2) solution, which is super
slow, so I want to think of a different way.

Right off the bat, I'm thinking of using a hash map for this problem, because at its core, a
"permutation" of s1 is just any substring that contains the same frequency of each unique
letter in s1. So, I need a frequency map, and a hash map is perfect for that, storing
each character of s1 and its frequency as a key-value pair.

Now I need a way to actually analyze the relevant substrings in s2, and a perfect way to do
this is to use the sliding window pattern, which is pretty useful for checking substrings
with conditions. In this case, the sliding window can actually be of a fixed size because
we know the length of the desired substring in s2 will be equal to the length of s1.
With sliding window, I can change the time complexity from O(n^2) to O(n).

NOTE: There's an edge case for this where they could just be annoying and give me a case
where s1 is just straight up longer than s2. In that case, there's no way for s2 to
be a permutation of s1 so I'll just return false immediately to avoid errors.

NOTE: There's another edge case where the frequencies match up immediately before I even 
begin iterating. In that case, I need to perform a check and return true.

Hash map implementation for frequency counting:
- To keep track of the character frequencies using hash maps, you need two separate maps.
- One will be for s1, the other will be for the substring in s2, which is represented
by the window I'm going to define.
- Since I'm using a window of fixed size, I'm going to make it start at the beginning of
s2, so to populate the initial character frequencies, I just iterate through the characters
in s1 and add to their corresponding frequencies in the s1 map, then iterate through the
characters contained in my window and add to their corresponding frequencies in my window
map.
- As I move the window, I will add to the frequency of whatever character enters my window
from the right, and remove from the frequency of whatever character leaves the window.
- If the count of a given character ever reaches 0 in my window, I need to remove it from
the hash map because otherwise when I equate the two hash maps its not going to say they're
inequal.

Actual Python Implementation:
1. Create the 2 hash maps to store the frequencies
2. Initialize the hash maps using something like frequencies[s[i]] = frequencies.get(s[i], 0) + 1
for each i less than the length of s1.
3. Define two pointers l and r to represent the left and right of the window of size s1.
4. Start l at 0 and start r at len(s1)
5. Slide the window along s2 using a for loop
6. Add to the frequency of the new char entering with frequencies[s[r]] = frequencies.get(s[r], 0) + 1
7. Subtract from the frequency of the char leaving from the left with frequencies[s[l]] -= 1
8. Check if the frequency of the char leaving is now 0, if so delete it with del.
9. Move the left pointer up with l += 1
10. Check for a match between the character frequencies using map1 == map2
11. If they match, return true.
12. If the loop ends and no matches were found, return false.
 
NOTE: The hash map solution is a way to do this and the first way I thought of when doing this problem,
but after solving this problem I found an another cool alternative way to do this that doesn't require
you to think of deleting the characters in the window map once they reach a frequency of 0. You can 
actually just do it with arrays instead if you run an algorithm to map characters to indices and use
an array of size 26 (one index for each letter). The "value" stored at those indices will represent
the frequency of that character.

Direct array implementation:
In python, you can actually use the ord() function on a character to get its ASCII value, and subtracting
the ASCII value of the character 'a' from any lowercase letter's ASCII value just perfectly gives you 
0-25 indices for each character. Once you have this mapping completed, you can just use each index to
represent the letters a-z and the values at each index to represent the mapping. This allows you
to skip the step where you need to delete elements if their frequencies = 0 because all the letters are
tracked regardless of if they even appear in s1 to begin with or not, it's just that their frequencies
will be stored with a value of 0, which you actually can directly equate across two arrays.
```

