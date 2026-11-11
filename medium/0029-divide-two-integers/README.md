# Divide Two Integers

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given two integers `dividend` and `divisor`, divide two integers **without** using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, `8.345` would be truncated to `8`, and `-2.7335` would be truncated to `-2`.

Return *the **quotient** after dividing *`dividend`* by *`divisor`.

**Note: **Assume we are dealing with an environment that could only store integers within the **32-bit** signed integer range: `[−231, 231 − 1]`. For this problem, if the quotient is **strictly greater than** `231 - 1`, then return `231 - 1`, and if the quotient is **strictly less than** `-231`, then return `-231`.

 

Original
Python3
**Example 1:**

```
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

```

**Example 2:**

```
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.

```

 

**Constraints:**

- -231 <= dividend, divisor <= 231 - 1
- divisor != 0

## Solution

**Language:** Python  
**Runtime:** 2 ms (beats 26.34%)  
**Memory:** 19 MB (beats 94.67%)  
**Submitted:** 2026-11-11T16:12:24.585Z  

```py
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        
        negative = (dividend < 0) ^ (divisor < 0)

        
        dvd = abs(dividend)
        dvs = abs(divisor)

        quotient = 0

        
        while dvd >= dvs:
            temp_divisor = dvs
            multiple = 1
            
            while dvd >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1

            dvd -= temp_divisor
            quotient += multiple

        if negative:
            quotient = -quotient

        
        return max(INT_MIN, min(INT_MAX, quotient))
```

---

[View on LeetCode](https://leetcode.com/problems/divide-two-integers/)