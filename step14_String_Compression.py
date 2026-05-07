'''string compression
example1 s= "aaabbc" output: "a3b2c1" because there are 3 'a's, 2 'b's and 1 'c' in the string
example2 s= "abc" output: "a1b1c1" because there
is 1 'a', 1 'b' and 1 'c' in the string
'''
def string_compression(s):
    result = "" #initialize an empty string to store the compressed result
    count = 1 #initialize a count variable to keep track of consecutive characters
    for i in range(1,len(s)): #iterate through the input string starting from the second character
        if s[i] == s[i-1]: #if the current character is the same as the previous character, increment the count
            count += 1
        else: #if the current character is different from the previous character, append the previous character and its count to the result string
            result += s[i-1] + str(count)
            count = 1 #reset the count for the new character
    # append the last character and its count
    result += s[-1] + str(count)
    return result
s = "aaabbc"
print(string_compression(s))
s = "abc"
print(string_compression(s))
'''tc o(n) where n is the length of the input string, sc o(n) for the result string in the worst case when all characters are unique'''
