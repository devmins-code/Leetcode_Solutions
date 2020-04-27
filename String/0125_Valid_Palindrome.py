'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

Input: "A man, a plan, a canal: Panama"
Output: true

Input: "race a car"
Output: false
'''

class Solution:
    ''' Approach #1 '''
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        filteredString = ""

        # Filter out Alpha-Numeric characters
        for char in s:
            if(char.isalnum()):
                filteredString += char

        l = len(filteredString)

        ''' Check If filtered string is palindrome '''
        # Iterate upto filteredString len//2
        # Check if characcter at left is equal to character at right
        # Character at right can be accessed by [l-idx-1] where l is length of string, 
        # idx is current index  
        for idx in range(0, l//2):
            if(filteredString[idx] != filteredString[l-idx-1]):
                return False

        return True


if __name__ == '__main__':
    sol = Solution()
    s = "A man, a plan, a canal: Panama"
    print(sol.isPalindrome(s))