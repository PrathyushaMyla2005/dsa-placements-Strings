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