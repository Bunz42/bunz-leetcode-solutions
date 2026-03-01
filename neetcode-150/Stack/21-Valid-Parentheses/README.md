# 21 - Valid Parentheses

**Difficulty:** Easy | **Link:** https://neetcode.io/problems/validate-parentheses/question

## 1. Problem Description
```text
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.
```

**Example 1:**
```text
Input: s = "[]"

Output: true
```

**Example 2:**
```text
Input: s = "([{}])"

Output: true
```

**Example 3:**
```text
Input: s = "[(])"

Output: false
```

**Constraints:**
```text
1 <= s.length <= 1000
```

## 2. My Approach
```text
You can brute force this problem by just going through the array and
removing any valid brackets until no more can be removed. If the string
is empty at the end, you know that the string was valid and you can
return true, otherwise return false. This is an O(n^2) solution, which
is pretty slow.

So, instead what I can do is use a Stack data structure to store the
characters in the string, and then all I need to do is push opening
brackets onto the stack, then whenever I see a closing bracket, I just
check the top of the stack to see if the associated opening bracket
is there. If not, the string isn't valid and you can return false. 
If it is, you just pop the opening bracket off the top of the stack
then repeat the process until either the stack is empty or you find
that the string is invalid.

Since you're only iterating through the string once and pushing and
popping occurs in constant O(1) time, the time complexity when you
use this stack algorithm is a faster O(n) solution!

Implementation (Python):
- Make a map (dictionary) of all the possible closing brackets and their associated
opening brackets in key-value pairs.
- Define the stack (you can just use a normal list in python
cause python is really easy)
- Push: stack.append(val)
- Pop: stack.pop(val)
- Peek: stack[-1]
- Checking if its empty: if not stack
- Iterate through each character in the array
- If the character is in the bracket map (a.k.a if its a closing bracket) then you
just pop the top of the stack (however, if the stack is empty at that time, you can't
pop anything off it so you need to make sure you don't get an error so use a dummy value "").
- If the char's opening bracket isn't in the stack, just return false instantly
- If the char is an opening bracket (so if it's not in the bracket map as a key), push it onto the stack
- Return "not stack" at the end because the stack has to be empty if the string is valid.
```

