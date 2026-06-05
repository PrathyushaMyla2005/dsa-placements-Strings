'''longest palindromic substring
Example 1:
Input: s = "babad"
Output: "bab" or "aba"'''
def longest_palindrome(s):
    left = 0 #initialize left pointer
    right = 0 #initialize right pointer
    for i in range(len(s)):
        odd = expand_around_center(s, i, i) #check for odd length palindrome
        even = expand_around_center(s, i, i + 1) #check for even length palindrome
        max_len = max(odd, even) #get the maximum length of palindrome found