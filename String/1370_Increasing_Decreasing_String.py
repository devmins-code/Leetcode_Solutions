'''
Given a string s. You should re-order the string using the following algorithm:

- Pick the smallest character from s and append it to the result.
- Pick the smallest character from s which is greater than the last appended character to the result and append it.
- Repeat step 2 until you cannot pick more characters.
- Pick the largest character from s and append it to the result.
- Pick the largest character from s which is smaller than the last appended character to the result and append it.
- Repeat step 5 until you cannot pick more characters.
- Repeat the steps from 1 to 6 until you pick all characters from s.
- In each step, If the smallest or the largest character appears more than once you can choose any occurrence and 
  append it to the result.

Return the result string after sorting s with this algorithm.

Constraints:
- 1 <= s.length <= 500
- s contains only lower-case English letters.

Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"

Input: s = "rat"
Output: "art"
'''

class Solution:
    ''' Approach #1 (Frequency array) '''
    def sortString(self, s: str) -> str:
        # Frequency list to count frequency of character in string s.
        # (Mapping of indexes): idx 0->a, 1->b, 2->c ... z->25. 
        frequency = [0]*26
        ans = ""; lengthAns = 0; lengthS = len(s)
        
        for char in s:
            # ord() return the ascii value of character
            # ord(char)-ord('a') returns the mapped index 
            # e.g. char = 'b' -> ord(char)-ord('a') =>  98-97 = 1  
            frequency[ord(char)-ord('a')] += 1

        while(lengthAns != lengthS):
            # Append char to ans in increasing order
            for idx in range(0,26):
                if(frequency[idx]!=0):
                    ans += chr(idx+ord('a'))
                    lengthAns += 1
                    # Decreasing frequency count after adding char to ans
                    frequency[idx] -= 1

            # Append char to ans in decreasing order
            for idx in range(26-1,-1,-1):
                if(frequency[idx]!=0):
                    ans += chr(idx+ord('a'))
                    lengthAns += 1
                    # Decreasing frequency count after adding char to ans
                    frequency[idx] -= 1
        
        return ans

if __name__ == '__main__':
    sol = Solution()
    s = "aaaabbbbcccc"
    print(sol.sortString(s))