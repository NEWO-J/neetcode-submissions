class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        built = []
        sum1 = 0
        candidates = sorted(candidates)
        def comb(built, target_remaining, start):
            nonlocal sum1
            nonlocal candidates
            if target_remaining == 0:
                result.append(built[:])
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > target_remaining:
                    return
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                else:
                    built.append(candidates[i])
                    sum1 += candidates[i]
                    comb(built, target_remaining - candidates[i], i + 1) 
                    sum1 -= built.pop()

        comb(built, target, 0)
        return result