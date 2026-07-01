class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        result = []
        for string in strs:
            sorted_list = sorted(string)
            abcstring = "".join(sorted_list)
            if abcstring in seen:
                seen[abcstring].append(string)
            else:
                seen[abcstring] = [string]
        for key in seen:
            result.append(seen[key])
        return result
                