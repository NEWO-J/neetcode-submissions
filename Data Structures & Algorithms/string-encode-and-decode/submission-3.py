class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for value in strs:
            # we must use a non-ascii char as delimiter
            encoded_string += (str(len(value)) + "#" + value) 
        return encoded_string

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            # 1. 'j' finds the separator
            while s[j] != "#":
                j += 1
            
            # 2. Extract length (everything between our anchor 'i' and separator 'j')
            length = int(s[i:j])
            
            # 3. Use the anchor 'j' to grab the string
            #    String starts at j + 1, and is 'length' characters long
            res.append(s[j + 1 : j + 1 + length])
            
            # 4. Teleport 'i' to the start of the NEXT metadata block
            i = j + 1 + length
            
        return res
        