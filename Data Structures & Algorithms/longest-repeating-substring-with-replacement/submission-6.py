class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # for each window, we will check the most frequent element
        # we will [1,1,2,2,0,2,2,0,1,1,1] <-- look at this. so we dont need to check the most freq element
        # This is a dynamic window problem
        # Maybe the window acts as the secction that we are replacing?
        # But how would we know the total substring length, thats what the window is for
        # Condition to shrink/grow the substring
            # Maybe subtract the most frequent element in our window from the total window size 
            # And see if its valid by checking if its equal to or less than k.
            # if less than k
                # continue traversing
            # if more than k
                # shrink window
        i = 0
        j = 0
        most_common = float('-inf')
        best_replacement = 0
        freq = collections.defaultdict(int)
        while j < len(s):
            freq[s[j]] += 1
            if freq[s[j]] > most_common:
                    most_common = freq[s[j]]
                    
            if ((j - i) + 1) - most_common <= k:
                    best_replacement = ((j - i) + 1)
            else:
                freq[s[i]] -= 1
                i += 1
            j += 1

        return best_replacement
                    
            # how do we update the CURRENT greatest element frequency, (not all time)
            # i.e how do we remove an old stale value of the greatest current frequency?

            
