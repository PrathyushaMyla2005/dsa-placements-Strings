'''convert a string to an integer
example1 s= "123" output: 123 because it is the integer representation of the input string
example2 s= "abc" output: None because it cannot be converted to an integer
example3 s= "12a3" output: None because it contains non-digit characters and cannot be converted to an integer
example4 s= "-123" output: -123 because it is the integer representation of the input string with a negative sign
'''
def string_to_integer(s):
    if s.startswith('-'): #check if the input string starts with a negative sign
        s = s[1:] #remove the negative sign for further processing
        sign = -1 #set the sign to negative
    else:
        sign = 1 #set the sign to positive
    if not s.isdigit(): #check if the remaining string contains only digits
        return None #if it contains non-digit characters, return None
    return sign * int(s) #convert the string to an integer and apply the sign
s = "123"
print(string_to_integer(s))
s = "abc"
print(string_to_integer(s))
s = "12a3"
print(string_to_integer(s))
s = "-123"
print(string_to_integer(s)) 
'''tc o(n) where n is the length of the input string, sc o(1) for the sign variable and the integer conversion process'''
def string_to_integer(s):
    number = int(s) #attempt to convert the string to an integer
    return number #return the converted integer
s = "123"
print(string_to_integer(s))
s = "abc"
print(string_to_integer(s))
'''tc o(n) where n is the length of the input string, sc o(1) for the integer conversion process'''