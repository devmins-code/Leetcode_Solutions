'''
Given an array arr, replace every element in that array with the greatest element among the elements to its right, 
and replace the last element with -1.After doing so, return the array.

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]

Constraints:
1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5
'''

from typing import List

class Solution:
    ''' Approach #1 '''
    ''' 
        Start from the end of the array with a variable storing current max value -1. 
        update the current max value while iterating from the end (right)  after updating your 
        List arr.
    '''
    def replaceElements(self, arr: List[int]) -> List[int]:
        currMax = -1
        for idx in range(len(arr)-1,-1,-1):
            # Store value of current element in a temp variable
            tempVal = arr[idx]
            # Assign currentMax to arr[idx] (current element)
            arr[idx] = currMax 
            # Update max value 
            currMax = max(currMax,tempVal)
        
        return arr


if __name__ == '__main__':
    sol = Solution()
    arr = [17,18,5,4,6,1]
    print(sol.replaceElements(arr))
