class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mostfreq = 0
        longest = 0
        l = 0
        r = 0
        char_map = defaultdict(int)
        for r in range(len(s)):
            char_map[s[r]] += 1
            mostfreq = max(mostfreq, char_map[s[r]])

            while (r - l + 1) - mostfreq > k:
                char_map[s[l]] -= 1
                l += 1
            
            longest = max(longest, (r - l + 1))
        
        return longest