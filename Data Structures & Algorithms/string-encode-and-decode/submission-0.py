class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for value in strs:
            # we must use a non-ascii char as delimiter
            encoded_string += value + "è"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        result = s.split("è")
        result.pop()
        return result
        