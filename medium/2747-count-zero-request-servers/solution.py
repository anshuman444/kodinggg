class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        
        logs.sort(key=lambda item: item[1])
        
       
        sorted_queries = sorted(enumerate(queries), key=lambda item: item[1])
        
        ans = [0] * len(queries)
        server_counts = [0] * (n + 1)
        active_servers = 0
        
        left = 0
        right = 0
        m = len(logs)
        
        for original_idx, q_time in sorted_queries:
            start_time = q_time - x
            end_time = q_time
            
            
            while right < m and logs[right][1] <= end_time:
                s_id = logs[right][0]
                if server_counts[s_id] == 0:
                    active_servers += 1
                server_counts[s_id] += 1
                right += 1
                
            
            while left < m and logs[left][1] < start_time:
                s_id = logs[left][0]
                server_counts[s_id] -= 1
                if server_counts[s_id] == 0:
                    active_servers -= 1
                left += 1
                
            
            ans[original_idx] = n - active_servers
            
        return ans