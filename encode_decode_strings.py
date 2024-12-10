class Solution:

    def encode(self, strs: List[str]) -> str:
        # Initialize an empty string to store the encoded result
        res = ""
        # Iterate through each string in the array
        for s in strs:
            # Append the length of the string, a delimiter, and the string itself to the result
            res += str(len(s)) + "$" + s
        # Return the encoded string
        return res

    def decode(self, s: str) -> List[str]:
        # Initialize an empty array to store the decoded strings
        res, i = [], 0

        # Iterate through the encoded string
        while i < len(s):
            # Find the position of the delimiter
            j = i
            while s[j] != "$":
                j += 1
            # Extract the length of the next string
            length = int(s[i:j])
            # Extract the string using the length and append it to the result array
            res.append(s[j + 1 : j + 1 + length])
            # Move the index to the start of the next encoded string
            i = j + 1 + length

        # Return the decoded array of strings
        return res