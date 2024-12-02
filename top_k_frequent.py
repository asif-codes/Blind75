class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a hashmap to count the frequency of each number
        count = {}
        # Create an array of empty lists to store numbers by their frequency
        freq = [[] for i in range(len(nums) + 1)]

        # Count the frequency of each number in the array
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Group numbers by their frequency
        for n, c in count.items():
            freq[c].append(n)

        # Create a result array to store the top k frequent numbers
        res = []
        # Iterate through the frequency array in reverse order
        for i in range(len(freq) - 1, 0, -1):
            # Add numbers to the result array until we have k numbers
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res