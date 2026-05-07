'''find the ascii value of a character]
example1 ch= 'a' output: 97 because the ascii value of 'a' is 97
example2 ch= 'A' output: 65 because the ascii value of 'A' is 65
'''
def ascii_value(ch):
    return ord(ch) #use the built-in ord() function to get the ascii value of the input character
ch = 'a'
print(ascii_value(ch))
ch = 'A'
print(ascii_value(ch))
'''tc o(1) for the ascii value retrieval process, sc o(1) for the space used to store the input character and the resulting ascii value'''