# Minimum Moves to Equal Array Elements II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums` of size `n`, return *the minimum number of moves required to make all array elements equal*.

In one move, you can increment or decrement an element of the array by `1`.

Test cases are designed so that the answer will fit in a **32-bit** integer.

 

**Example 1:**

```
Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

```

**Example 2:**

```
Input: nums = [1,10,2,9]
Output: 16

```

 

**Constraints:**

- n == nums.length
- 1 <= nums.length <= 105
- -109 <= nums[i] <= 109

## Solution

**Language:** Python  
**Runtime:** 5 ms (beats 43.62%)  
**Memory:** 20.3 MB (beats 93.87%)  
**Submitted:** 2026-11-02T16:01:22.876Z  

```py
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        moves = 0
        left, right = 0, len(nums) - 1
        
        while left < right:
            moves += nums[right] - nums[left]
            left += 1
            right -= 1
            
        return moves
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/)