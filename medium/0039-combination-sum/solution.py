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