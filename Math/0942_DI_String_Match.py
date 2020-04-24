'''
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]
 
Input: "IDID"
Output: [0,4,1,3,2]

Input: "III"
Output: [0,1,2,3]

Input: "DDI"
Output: [3,2,0,1]
'''

from typing import List
class Solution:
    ''' Approach #1 (Greedy) '''
    '''
        Initialize I and D with 0 and len(S) respectively
        for each 'I' occurence in S append variable I in a list and increment I by 1
        for each 'D' occurence in S append variable D in a list and decrement D by 1
    '''
    def diStringMatch(self, S: str) -> List[int]:
        I = 0; D = len(S)
        ret = list()
        for char in S:
            if(char=='D'):
                ret.append(D)
                D -= 1
            else:
                ret.append(I)
                I += 1
        
        # Append either I or D in the end for the remaining integer
        ret.append(I)
        return ret


if __name__ == '__main__':
    sol = Solution()
    S = "IDID"
    print(sol.diStringMatch(S))