class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 0
        most_common = float('-inf')
        best_replacement = 0
        freq = collections.defaultdict(int)
        while j < len(s):
            freq[s[j]] += 1
            if freq[s[j]] > most_common:
                    most_common = freq[s[j]]
                    
            if ((j - i) + 1) - most_common <= k:
                    best_replacement = ((j - i) + 1)
            else:
                freq[s[i]] -= 1
                i += 1
            j += 1

        return best_replacement

            
