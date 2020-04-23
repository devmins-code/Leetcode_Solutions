'''
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

class Solution:
    ''' Approach #1 (Dynamic Programming) '''
    '''
        One can Reach ith step by:
            - Taking one step from (i-1)th step
            - Taking two step from (i-2)th step
        So, Total number of ways to reach will be sum of ways to reach (i-1)th step and (i-2)th step
    '''

    def climbStairs(self, n: int) -> int:
        if(n<2):return 1
        # Initializing dp list
        dp = [0]*(n+1)
        # For n=1 total_ways = 1
        # For n=2 total_ways = 2  
        dp[1] = 1
        dp[2] = 2 
        for step in range(3,len(dp)):
            dp[step] = dp[step-1] + dp[step-2]
        
        return dp[n]

if __name__ == '__main__':
    sol = Solution()
    n = 3
    print(sol.climbStairs(n))
