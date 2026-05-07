'''first repating character in a string
example1 s= "hello world" output: 'l' because it is the first character
that repeats in the string
example2 s= "abc" output: None because there are no repeating characters in the string
'''
def first_repeating_char(s):
    seen = set() #initialize an empty set to keep track of seen characters
    for char in s: #iterate through each character in the input string
        if char in seen: #if the character has been seen before, return it as the first repeating character
            return char
        seen.add(char) #mark the character as seen by adding it to the set
    return None #if no repeating character is found, return None
s = "hello world"
print(first_repeating_char(s))
s = "aabc"
print(first_repeating_char(s))
'''tc o(n) where n is the length of the input string, sc o(m) where m is the number of unique characters in the input string for the seen set'''
