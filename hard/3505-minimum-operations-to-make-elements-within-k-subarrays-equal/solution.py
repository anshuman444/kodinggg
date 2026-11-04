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