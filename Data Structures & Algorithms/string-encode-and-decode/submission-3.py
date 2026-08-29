class Solution:

    def encode(self, strs: List[str]) -> str:
        # variable to store encoded string
        encoded = "";
        # loop through strings
        for i in strs:
            # append length of string + separator # + word
            encoded += str(len(i)) + "#" + i
        return encoded
        
    def decode(self, s: str) -> List[str]:
        print(s)
        # array for decoded words
        # initialise pointer i to 0
        decoded, i = [], 0
        # loop through string while i is less than length of string
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            decoded.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return decoded
