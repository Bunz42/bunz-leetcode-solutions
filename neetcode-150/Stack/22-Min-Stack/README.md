# 22 - Min Stack

**Difficulty:** Medium | **Link:** https://neetcode.io/problems/minimum-stack/question

## 1. Problem Description
```text
Design a stack class that supports the push, pop, top, and getMin operations.

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in O(1) time.
```

**Example 1:**
```text
Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

Output: [null,null,null,null,0,null,2,1]

Explanation:
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1
```

**Constraints:**
```text
-2^31 <= val <= 2^31 - 1.
pop, top and getMin will always be called on non-empty stacks.
```

## 2. My Approach
```text
This problem is kind of weird, because it's a class design problem.
Essentially, this problem is just designing a stack class but with 
an extra feature added that allows for the lookup of the minimum
value in the stack.

To implement this class, I'll start by just implementing the constructor
and functions for a basic stack class using python's stack functionality.

Constructor: just initialize a self.stack = []
Push: just push an element onto the stack with self.stack.append(val)
Pop: self.stack.pop()
Top: return self.stack[-1] to peek at the top element

Now, we need to implement the getMin() function, which is the special part
of this problem. To do this, I need a way to locate the minimum element in
the stack. Now, a brute force approach to implementing this function would
be to just iterate through the stack and find the minimum element, but the
problem says all the functions need to run in O(1) time, so that O(n)
algorithm isn't going to work out.

So, I need a way to get the time complexity down to O(1), and one way I 
can think of to do that is just to use another stack, since popping and
pushing into a stack is an O(1) operation, if I just create another stack
to keep track of the minimum element in any stack created by this class,
I can implement the getMin() function.

I'm going to do this by initializing another stack called min_stack in
my constructor, then updating my push() method to append elements to not
only the actual stack, but also the min_stack. The min_stack will be empty at the 
start, so I need to perform a check to see if its empty. If it is, I'll just push
the value directly because it's guaranteed to be a minimum at that point.
Then, anytime after that, I'll push the minimum between the desired value and the
previously found minimum onto the stack, which will guarantee the smallest value
in the stack is always at the top of the min stack, while also guaranteeing that
the stacks are aligned in terms of size.

Of course, this means that whenever I pop from the stack, I need to pop from the
min stack as well to maintain size alignment.

Then, to implement the getMin() function, I just have to return the element at
the top of the min_stack, because its guaranteed to be the minimum.
```

