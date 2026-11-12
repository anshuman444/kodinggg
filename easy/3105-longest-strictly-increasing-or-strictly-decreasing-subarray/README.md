# Longest Strictly Increasing or Strictly Decreasing Subarray

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given an array of integers `nums`. Return *the length of the **longest** subarray of *`nums`* which is either **strictly increasing** or **strictly decreasing***.

 

Original
Python3
**Example 1:**

**Input:** nums = [1,4,3,3,2]

**Output:** 2

**Explanation:**

The strictly increasing subarrays of `nums` are `[1]`, `[2]`, `[3]`, `[3]`, `[4]`, and `[1,4]`.

The strictly decreasing subarrays of `nums` are `[1]`, `[2]`, `[3]`, `[3]`, `[4]`, `[3,2]`, and `[4,3]`.

Hence, we return `2`.

**Example 2:**

**Input:** nums = [3,3,3,3]

**Output:** 1

**Explanation:**

The strictly increasing subarrays of `nums` are `[3]`, `[3]`, `[3]`, and `[3]`.

The strictly decreasing subarrays of `nums` are `[3]`, `[3]`, `[3]`, and `[3]`.

Hence, we return `1`.

**Example 3:**

**Input:** nums = [3,2,1]

**Output:** 3

**Explanation:**

The strictly increasing subarrays of `nums` are `[3]`, `[2]`, and `[1]`.

The strictly decreasing subarrays of `nums` are `[3]`, `[2]`, `[1]`, `[3,2]`, `[2,1]`, and `[3,2,1]`.

Hence, we return `3`.

 

**Constraints:**

- 1 <= nums.length <= 50
- 1 <= nums[i] <= 50

## Solution

**Language:** Python  
**Runtime:** 1 ms (beats 58.21%)  
**Memory:** 19 MB (beats 93.87%)  
**Submitted:** 2026-11-12T18:23:25.166Z  

```py
class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        if not nums:
            return 0
            
        max_len = 1
        inc = 1
        dec = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            else:
                inc = 1
                dec = 1
                
            max_len = max(max_len, inc, dec)
            
        return max_len
```

---

[View on LeetCode](https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/)