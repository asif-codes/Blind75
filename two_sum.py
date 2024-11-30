class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a hashmap to store the indices of the numbers we have seen
        prevMap = {}

        # Iterate through the array of numbers
        for i, n in enumerate(nums):
            # Calculate the difference needed to reach the target
            diff = target - n
            # If the difference is already in the hashmap, return the indices
            if diff in prevMap:
                return [prevMap[diff], i]
            # Otherwise, add the current number and its index to the hashmap
            prevMap[n] = i