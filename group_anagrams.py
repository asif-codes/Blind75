class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a hashmap to store the grouped anagrams
        res = defaultdict(list)

        # Iterate through each string in the array
        for s in strs:
            # Create a count array to count the frequency of each character
            count = [0] * 26

            # Iterate through each character in the string
            for c in s:
                # Increment the count for the character
                count[ord(c) - ord('a')] += 1

            # Use the count array as a key and append the string to the corresponding array
            res[tuple(count)].append(s)
        
        # Return the grouped anagrams as a array of arrays
        return list(res.values())