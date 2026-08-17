class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        
        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursion level
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # Prune: no point continuing if this candidate already exceeds remaining
                if candidates[i] > remaining:
                    break
                
                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i], path)  # i+1: each number used once
                path.pop()  # undo the choice, try the next option
        
        backtrack(0, target, [])
        return result

candidates = [10,1,2,7,6,1,5]
target = 8

s = Solution()
print(s.combinationSum2(candidates=candidates, target=target))