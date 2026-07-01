class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = collections.defaultdict(int)
        smap = collections.defaultdict(int)
        have = 0
        need = 0
        minwin = float('inf')
        minsub = ""
        for i in t:
            if i not in tmap:
                need += 1
            tmap[i] += 1

        i = 0
        j = 0
        while j < len(s):
            if s[j] in tmap:
                smap[s[j]] += 1
                if smap[s[j]] == tmap[s[j]]:
                    have += 1
        
            while have == need:
                if j - i < minwin:
                    minwin = j - i
                    minsub = s[i:j+1]
         
                left_char = s[i]
                if left_char in smap:
                    smap[left_char] -= 1
                    # FIXED: Only decrement 'have' if we fall BELOW the required count
                    if smap[left_char] < tmap[left_char]:
                        have -= 1
                
                i += 1
            j += 1

        return minsub

                
            
        