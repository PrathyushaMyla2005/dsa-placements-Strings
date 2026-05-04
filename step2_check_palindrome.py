'''check if a string is a palindrome
example "madam" is a palindrome because it reads the same backward and forward
"hello" is not a palindrome because it reads "olleh" backward
'''
def is_palindrome(s):
    return s == s[::-1]
s = "madam"
print(is_palindrome(s))
s = "hello"
print(is_palindrome(s))
#use without slicing
def is_palindrome(s):
    left = 0 #start of the string
    right = len(s) - 1 #end of the string
    while left < right:
        if s[left] != s[right]: #if the characters at the left and right pointers are not the same, then it's not a palindrome
            return False
        left += 1#move the left pointer to the right
        right -= 1#move the right pointer to the left
    return True #if we have checked all characters and they are the same, then it's a palindrome
s = "madam"
print(is_palindrome(s))
s = "hello"
print(is_palindrome(s))
