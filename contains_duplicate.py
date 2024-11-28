class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create a set to store the numbers that have been seen
        seen = set()

        # Iterate through the numbers
        for num in nums:
            # If the number has been seen before, return True
            if num in seen:
                return True
            # Otherwise, add the number to the set
            seen.add(num)
        # If no duplicates are found, return False
        return False