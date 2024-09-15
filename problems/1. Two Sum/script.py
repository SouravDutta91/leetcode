from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Create a dictionary to store the value and its index
        seen = {}

        # Loop through the list of numbers
        for i, num in enumerate(nums):

            # Calculate the complement that we need to find
            complement = target - num

            # Check if the complement exists in the dictionary
            if complement in seen:

                # If found, return the index
                return [seen[complement], i]
            
            # If not found, store the current number with its index
            seen[num] = i


# main function
def main():

    # create an instance of the Solution class
    solution = Solution()
    
    # Example 1 from the problem
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(solution.twoSum(nums1, target1))

    # Example 2 from the problem
    nums2 = [3, 2, 4]
    target2 = 6
    print(solution.twoSum(nums2, target2))

    # Example 3 from the problem
    nums3 = [3, 3]
    target3 = 6
    print(solution.twoSum(nums3, target3))


# Run the main function
if __name__ == "__main__":
    main()