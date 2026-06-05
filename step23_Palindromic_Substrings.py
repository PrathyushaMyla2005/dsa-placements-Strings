'''find the palindromic substrings in a string

Example:
Input: s = "abc"
Output: 3
'''

def count_substrings(s):
    
    count = 0  # stores total palindrome substrings
    
    
    # function to expand from center
    def expand(left, right):
        
        palindromic_count = 0
        
        # check boundary and palindrome condition
        while left >= 0 and right < len(s) and s[left] == s[right]:
            
            palindromic_count += 1   # one palindrome found
            
            left -= 1   # move left pointer
            right += 1  # move right pointer
        
        return palindromic_count
    
    
    # take every character as center
    for i in range(len(s)):
        
        # odd length palindrome
        count += expand(i, i)
        
        # even length palindrome
        count += expand(i, i+1)
    
    
    return count


s = "abc"
print(count_substrings(s))