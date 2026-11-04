# Minimum Operations to Make Elements Within K Subarrays Equal

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given an integer array `nums` and two integers, `x` and `k`. You can perform the following operation any number of times (**including zero**):

- Increase or decrease any element of nums by 1.

Return the **minimum** number of operations needed to have **at least** `k` *non-overlapping subarrays* of size **exactly** `x` in `nums`, where all elements within each subarray are equal.

 

**Example 1:**

**Input:** nums = [5,-2,1,3,7,3,6,4,-1], x = 3, k = 2

**Output:** 8

**Explanation:**

- Use 3 operations to add 3 to nums[1] and use 2 operations to subtract 2 from nums[3]. The resulting array is [5, 1, 1, 1, 7, 3, 6, 4, -1].
- Use 1 operation to add 1 to nums[5] and use 2 operations to subtract 2 from nums[6]. The resulting array is [5, 1, 1, 1, 7, 4, 4, 4, -1].
- Now, all elements within each subarray [1, 1, 1] (from indices 1 to 3) and [4, 4, 4] (from indices 5 to 7) are equal. Since 8 total operations were used, 8 is the output.

**Example 2:**

**Input:** nums = [9,-2,-2,-2,1,5], x = 2, k = 2

**Output:** 3

**Explanation:**

- Use 3 operations to subtract 3 from nums[4]. The resulting array is [9, -2, -2, -2, -2, 5].
- Now, all elements within each subarray [-2, -2] (from indices 1 to 2) and [-2, -2] (from indices 3 to 4) are equal. Since 3 operations were used, 3 is the output.

 

**Constraints:**

- 2 <= nums.length <= 105
- -106 <= nums[i] <= 106
- 2 <= x <= nums.length
- 1 <= k <= 15
- 2 <= k * x <= nums.length

## Solution

**Language:** Python  
**Runtime:** 4833 ms (beats 34.61%)  
**Memory:** 52.7 MB (beats 46.15%)  
**Submitted:** 2026-11-04T16:39:43.210Z  

```py
from sortedcontainers import SortedList


class Solution:

  def minOperations(self, nums: list[int], x: int, k: int) -> int:
    n = len(nums)

   
    cost = [0] * n
    sl = SortedList()

    
    half = (x + 1) // 2
    left_sum = 0
    right_sum = 0

    for i in range(n):
      val = nums[i]
      idx = sl.bisect_left(val)
      sl.add(val)

      
      if idx < half:
        left_sum += val
        if len(sl) > half:
          
          promoted = sl[half]
          left_sum -= promoted
          right_sum += promoted
      else:
        right_sum += val

      
      if i >= x:
        out = nums[i - x]
        out_idx = sl.index(out)
        sl.remove(out)
        if out_idx < half:
          left_sum -= out
          if len(sl) >= half:
           
            demoted = sl[half - 1]
            right_sum -= demoted
            left_sum += demoted
        else:
          right_sum -= out

     
      if i >= x - 1:
        median = sl[half - 1]
        cost[i] = (half * median - left_sum) + (
            right_sum - (x - half) * median
        )

    
    INF = float("inf")
    
    dp = [[INF] * (k + 1) for _ in range(n + 1)]

    for i in range(n + 1):
      dp[i][0] = 0

    for i in range(1, n + 1):
      for j in range(1, k + 1):
        
        dp[i][j] = dp[i - 1][j]

        
        if i >= x:
          dp[i][j] = min(dp[i][j], dp[i - x][j - 1] + cost[i - 1])

    return dp[n][k]
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/)