'''
You're given strings J representing the types of stones that are jewels, and S representing the 
stones you have.  Each character in S is a type of stone you have.  You want to know how many of 
the stones you have are also jewels.
The letters in J are guaranteed distinct, and all characters in J and S are letters. 
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Input: J = "aA", S = "aAAbbbb"
Output: 3

Input: J = "z", S = "ZZ"
Output: 0
'''

class Solution:
    ''' Approach #1 (Hash Table) '''
    '''
        Store every Jewel as a key in the Hash Table
        Iterate over stones and in the jewel count if stone is present in the Hash 
    '''
    def numJewelsInStones(self, J: str, S: str) -> int:
        Hash = dict()
        jewelCount = 0
        for jewel in J:
            Hash[jewel] = True
        
        for stone in S:
            jewelCount += 1 if(stone in Hash) else 0
                
        return jewelCount

if __name__ == '__main__':
    sol = Solution()
    J = "aA"; S = "aAAbbbb"
    print(sol.numJewelsInStones(J,S))