'''
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''
from typing import List
class Solution:
    ''' Approach #1 (Kadane's Algorithm) '''
    '''
        Simple idea of the Kadane’s algorithm is to look for all positive contiguous segments 
        of the array (max_ending_here is used for this). And keep track of maximum sum contiguous 
        segment among all positive segments (max_so_far is used for this). 
        Each time we get a positive sum compare it with max_so_far and update max_so_far 
        if it is greater than max_so_far
        Reference: https://en.wikipedia.org/wiki/Maximum_subarray_problem
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        curr = nums[0]
        for idx in range(1,len(nums)):
            curr = max(curr+nums[idx],nums[idx])
            best = max(curr,best)
        
        return best


if __name__ == '__main__':
    sol = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(sol.maxSubArray(nums))