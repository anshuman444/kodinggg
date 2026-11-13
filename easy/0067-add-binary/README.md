# Add Binary

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two binary strings `a` and `b`, return *their sum as a binary string*.

 

Original
Python3
**Example 1:**

```
Input: a = "11", b = "1"
Output: "100"

```

**Example 2:**

```
Input: a = "1010", b = "1011"
Output: "10101"

```

 

**Constraints:**

- 1 <= a.length, b.length <= 104
- a and b consist only of '0' or '1' characters.
- Each string does not contain leading zeros except for the zero itself.

## Solution

**Language:** Python  
**Runtime:** 2 ms (beats 47.09%)  
**Memory:** 19.2 MB (beats 71.68%)  
**Submitted:** 2026-11-13T16:27:52.688Z  

```py
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
                
            res.append(str(total % 2))
            carry = total // 2
            
        return "".join(reversed(res))
```

---

[View on LeetCode](https://leetcode.com/problems/add-binary/)