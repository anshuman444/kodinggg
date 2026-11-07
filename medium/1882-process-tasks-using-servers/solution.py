import heapq
from typing import List


class Solution:

  def assignTasks(
      self, servers: List[int], tasks: List[int]
  ) -> List[int]:
    # Min-heap of available servers: (weight, index)
    available = [(w, i) for i, w in enumerate(servers)]
    heapq.heapify(available)

    # Min-heap of busy servers: (free_time, weight, index)
    busy = []

    ans = []
    current_time = 0

    for j, task_duration in enumerate(tasks):
      # Task j is not available until second j
      current_time = max(current_time, j)

      # If no servers are available, jump time to when the next busy server finishes
      if not available:
        current_time = busy[0][0]

      # Release all servers that have completed their tasks by current_time
      while busy and busy[0][0] <= current_time:
        free_time, weight, idx = heapq.heappop(busy)
        heapq.heappush(available, (weight, idx))

      # Assign the highest-priority available server to task j
      weight, idx = heapq.heappop(available)
      ans.append(idx)
      heapq.heappush(busy, (current_time + task_duration, weight, idx))

    return ans