'''
Given a string, sort it in decreasing order based on the frequency of characters.

Input:
"tree"
Output:
"eert"
Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Input:
"cccaaa"
Output:
"cccaaa"

Input:
"Aabb"
Output:
"bbAa"
Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''

class Solution:
    ''' Approach #1 (Hash Table) '''
    '''
    Count the frequency of each letter and then sort them according to frequency in decreasing order
    '''
    def frequencySort(self, s: str) -> str:
        # Dictionary to store Frequency
        Hash = dict()

        for letter in s:
            if(letter in Hash):
                Hash[letter] += 1
            else:
                Hash[letter] = 1
        
        # Hash.items() Return object of dict_items -> (key, value)
        itemList = list(Hash.items())
        # Sorting itemList according to frequency in decreasing order
        itemList.sort(key=lambda x:(x[1],x[0]), reverse=True)
        
        string = ""
        for item in itemList:
            # Repeat letter frequency (item[1]) times
            string += item[0]*item[1]
            
        return string
    

if __name__ == '__main__':
    sol = Solution()
    s = "tree"
    print(sol.frequencySort(s))