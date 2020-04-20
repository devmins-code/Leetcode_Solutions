'''
Given a string s and an integer k. You should construct k non-empty palindrome strings using all the characters in s.
Return True if you can use all the characters in s to construct k palindrome strings or False otherwise.
Example 1:
Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"
Example 2:

Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.
'''

class Solution:
    ''' Approach #1 (Using Frequency Array)'''
    ''' 
    If the number of characters that have odd counts is > k then the minimum number of palindrome strings 
    we can construct is > k and answer is false. 
    '''
    def canConstruct(self, s: str, k: int) -> bool:
        lenS = len(s)
        if(k>lenS):return False
        if(k==lenS):return True
        
        # Frequency list to count frequency of character in string s.
        # (Mapping of indexes): idx 0->a, 1->b, 2->c ... z->25. 
        frequency = [0]*26; odd = 0
        for char in s:
            # ord() return the ascii value of character
            # ord(char)-ord('a') returns the mapped index 
            # e.g. char = 'b' -> ord(char)-ord('a') =>  98-97 = 1
            frequency[ord(char)-ord('a')] += 1
            
        for val in frequency:
            if(val%2!=0):
                odd += 1
                # If odd count is > k return False
                if(odd>k):
                    return False
        return True

if __name__ == '__main__':
    sol = Solution()
    s = "annabelle"; k = 2
    print(sol.canConstruct(s,k))