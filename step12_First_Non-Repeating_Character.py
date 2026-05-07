'''first non-repeating character in a string
example1 s= "hello world" output: 'h' because it is the first character that does not repeat in the string
example2 s= "aabbcc" output: None because all characters repeat in the string
'''
def first_non_repeating_char(s):
    char_count = {} #initialize an empty dictionary to store the count of each character
    for char in s: #iterate through each character in the input string
        if char in char_count: #if the character is already in the count dictionary, increment its count
            char_count[char] += 1
        else: #if the character is not in the count dictionary, add it with a count of 1
            char_count[char] = 1
    for char in s: #iterate through the input string again to find the first non-repeating character
        if char_count[char] == 1: #if the count of the character is 1, return it as the first non-repeating character
            return char
    return None #if no non-repeating character is found, return None
s = "hello world"
print(first_non_repeating_char(s))
s = "aabbcc"
print(first_non_repeating_char(s))
'''tc o(n) where n is the length of the input string, sc o(m)
where m is the number of unique characters in the input string for the char_count dictionary'''
