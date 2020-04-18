'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Input: nums = [2, 7, 11, 15], target = 9
Output: return [0, 1]
Explanation nums[0] + nums[1] = 2 + 7 = 9
'''

from typing import List
class Solution:
    ''' Approach #1 (Using Hash Table)'''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store nums and their index
        # Dictionary key stores the number and its value store the index for the respective number
        Hash = dict()
        for idx in range(0,len(nums)):
            counterPart = target-nums[idx]

            # Check if target-currentnumber (counter part) is present in Hash
            # In case of above example 9-2=7 (7 will be present in the Hash) so index of 2 and 7 are the result 
            if((counterPart in Hash) and idx!=Hash[counterPart]):
                return [Hash[counterPart],idx]
            
            # Update the Hash for current index  
            Hash[nums[idx]] = idx


if __name__ == '__main__':
    sol = Solution()
    nums = [2, 7, 11, 15]; target = 9
    print(sol.twoSum(nums,target))