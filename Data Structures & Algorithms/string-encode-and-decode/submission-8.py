class Solution:


    def encode(self, strs: List[str]) -> str:
        endstring = ""
        for i in strs:
            endstring += f"{len(i)}#{i}"
        return endstring

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            jump = ""
            while s[i] != '#':
                jump += s[i]
                i += 1
            decoded.append(s[i + 1:i + int(jump) + 1])
            i += int(jump) + 1

        return decoded