class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        current_best = 0
        subs = []
        l = 0
        r = 0
        while l < (len(s) - 1) and r < (len(s)):
            if s[r] not in subs:
                subs.append(s[r])
                if (r-l+1) > current_best:
                    current_best = (r-l+1)
                r += 1
            else:
                l += 1               
                subs.pop(0)
          

        return current_best