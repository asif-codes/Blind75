class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths of the strings are not equal, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Create hashmaps to count the frequency of each character in both strings
        countT, countS = {}, {}

        # Iterate through the characters of both strings
        for i in range(len(s)):
            # Increment the count for the character in the first string
            countS[s[i]] = 1 + countS.get(s[i], 0)
            # Increment the count for the character in the second string
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # Compare the character counts in both hashmaps
        for c in countS:
            # If the counts do not match, the strings are not anagrams
            if countS[c] != countT.get(c, 0):
                return False
        
        # If all counts match, the strings are anagrams
        return True