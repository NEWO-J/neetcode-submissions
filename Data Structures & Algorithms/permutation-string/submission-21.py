class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = collections.defaultdict(int)
        freq2 = collections.defaultdict(int)
    
        for i in s1:
            freq[i] += 1
       
        i = 0
        j = 0
        while j < len(s2):
            if s2[j] in freq:
                if not freq2:
                    i = j
                freq2[s2[j]] += 1
            else:
                while i < j:
                    if s2[i] in freq2:
                        freq2[s2[i]] -= 1
                        if freq2[s2[i]] == 0:
                            del freq2[s2[i]]
                    i += 1  
            if (j - i) + 1 == len(s1):
                if freq == freq2:
                    return True
            j += 1
            if (j - i) + 1 > len(s1):
                freq2[s2[i]] -= 1
                i += 1


        return False
  