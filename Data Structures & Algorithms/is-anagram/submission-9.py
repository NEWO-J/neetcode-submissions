class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = [0] * 26
        for i in s:
            seen[ord(i) - ord('a')] += 1
        seen2 = [0] * 26
        for i in t:
            seen2[ord(i) - ord('a')] += 1
        
        if seen == seen2:
            return True
        
        return False
            