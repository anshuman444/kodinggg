# Combination Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array of **distinct** integers `candidates` and a target integer `target`, return *a list of all **unique combinations** of *`candidates`* where the chosen numbers sum to *`target`*.* You may return the combinations in **any order**.

The **same** number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input.

 

Original
Python3
**Example 1:**

```
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

```

**Example 2:**

```
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

```

**Example 3:**

```
Input: candidates = [2], target = 1
Output: []

```

 

**Constraints:**

- 1 <= candidates.length <= 30
- 2 <= candidates[i] <= 40
- All elements of candidates are distinct.
- 1 <= target <= 40

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 93.66%)  
**Memory:** 19.3 MB (beats 93.38%)  
**Submitted:** 2026-11-18T16:01:28.278Z  

```py
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()  # Enables early pruning

        def backtrack(start: int, path: List[int], remaining: int) -> None:
            if remaining == 0:
                result.append(path.copy())
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break  # Prune: all subsequent elements are also too large

                path.append(candidates[i])
                # Pass `i` (not `i + 1`) because the same element can be reused
                backtrack(i, path, remaining - candidates[i])
                path.pop()  # Backtrack

        backtrack(0, [], target)
        return result
```

---

[View on LeetCode](https://leetcode.com/problems/combination-sum/)