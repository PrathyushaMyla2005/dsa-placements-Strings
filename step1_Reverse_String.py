''' reverse the string'''
def reverse(s):
    return s[::-1]
s = "hello"
print(reverse(s))
#use without slicing
def reverse(s):
    result = " "
    for i in s:
        result = i + result #this is the key point, we are adding the current character before the result string
    return result
s = "hello"
print(reverse(s))
'''tc o(n) where n is length of input string, sc o(n) for result string'''

def reverse(s):
    left = 0#initialize the left pointer to the start of the string
    right = len(s) - 1#initialize the right pointer to the end of the string
    while left < right:#while the left pointer is less than the right pointer, swap the characters at the left and right pointers and move the pointers towards the center
        s[left], s[right] = s[right], s[left]#swap the characters at the left and right pointers
        left += 1#move the left pointer to the right
        right -= 1#move the right pointer to the left
    return s#return the reversed string
s = ["h","e","l","l","o"]
print(reverse(s))
'''tc o(n) where n is length of input string, sc o(1) because we are reversing the string in place without using any extra space.'''


