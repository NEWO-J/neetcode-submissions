class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        current_best = 0
        subs = set()
        l = 0
        r = 0
        while l < (len(s) - 1) and r < (len(s)):
            if s[r] not in subs:
                subs.add(s[r])
                if (r-l+1) > current_best:
                    current_best = (r-l+1)
                r += 1
            else:
                subs.remove(s[l])
                l += 1               
          
        return current_best