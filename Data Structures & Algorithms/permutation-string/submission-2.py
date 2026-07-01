class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        freq2 = {}
        window = []
        for i in s1:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        print(freq)

 
        i = 0
        j = len(s1)
        window = [s2[i]]
        while j < len(s2) + 1:
            for char in s2[i:j]:
                if char in freq2:
                    freq2[char] += 1
                else:
                    freq2[char] = 1
            if freq2 == freq:
                return True
            
            freq2 = {}
            i += 1
            j += 1
            
            
        return False
            