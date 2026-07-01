class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = collections.defaultdict(int)
        i = 0
        j = 0
        longest = 0
        while j < len(s):
            if freq[s[j]] == 0:
                freq[s[j]] += 1
                j += 1
            else:
                longest = max(longest, j - i)
                while s[i] != s[j]:
                    freq[s[i]] -= 1
                    i += 1
                
                freq[s[i]] -= 1
                i += 1
                freq[s[j]] += 1
                j += 1

            
            longest = max(longest, j - i)

        return longest