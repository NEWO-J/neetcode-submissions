class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lmap2 = collections.defaultdict(list)
        result = []
        for s in strs:
            freq = [0 for _ in range(26)]
            for char in s:
                freq[ord(char) - ord('a')] += 1
            freq = tuple(freq)    
            lmap2[freq].append(s)
        
        for key,value in lmap2.items():
            result.append(value)
        
        return result
            
                