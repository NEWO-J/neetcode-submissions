class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i = 0
        j = 0
        num_unique = 0
        freq1 = collections.Counter(t)
        freq2 = collections.defaultdict(int)


        min_substr = ""
        min_len = float('inf') 

        while j < len(s):
            if s[j] in freq1:
                freq2[s[j]] += 1
                if freq2[s[j]] == freq1[s[j]]:
                    num_unique += 1
            

            while num_unique == len(freq1):
                if (j - i + 1) < min_len:
                    min_substr = s[i:j + 1]
                    min_len = j-i + 1

                left_char = s[i]
                if left_char in freq1:
                    if freq2[left_char] == freq1[left_char]:
                        num_unique -= 1
                    freq2[left_char] -= 1
                i += 1
            j += 1    

        return min_substr
            
                    