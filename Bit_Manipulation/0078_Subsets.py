'''
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

from typing import List
import math
class Solution:
    ''' Approach #1 '''
    '''
    This approach use the binary value of 0 to pow(2,len(nums))-1
    and append nums[idx] to set where idx is the set bit (1) of the
    binary representation.

    nums  = [1,2,3]
    combos = pow(2, 3) = 8
    Run for binary counter = 000 to 111

    Value of Counter            Subset
        000                    -> []
        001                    -> [1]
        010                    -> [2]
        011                    -> [1,2]
        100                    -> [3]
        101                    -> [1,3]
        110                    -> [2,3]
        111                    -> [1,2,3]
    Resources: https://en.wikipedia.org/wiki/Power_set
    '''

    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Find total combos
        combos = int(math.pow(2,len(nums)))
        powerSet = list()
        for decimal in range(0,combos):
            idx = 0
            newSubSet = list()
            while(decimal):
                # check if the rightmost bit is 1 
                # (decimal & 1) returns 1 if rightmost bit is 1 else 0
                # you can also check if the decimal value is odd instead. 
                if(decimal & 1):
                    # Append nums[idx] to newSubSet if rightmost bit is 1
                    newSubSet.append(nums[idx])                
                
                idx += 1
                # Right shifting decimal by one bit
                # You can also use int(decimal/2) instead of right shift both will have same result
                decimal >>= 1
            
            powerSet.append(newSubSet)
        
        return powerSet

if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3]
    print(sol.subsets(nums))