''' remove duplicates in the string and return the new string.
example1 s= "hello world" becomes "helo wrd"  '''
def remove_duplicates(s):
    seen = set() #initialize an empty set to keep track of seen characters
    result = "" #initialize an empty string to store the result
    for char in s: #iterate through each character in the input string
        if char not in seen:#if the character has not been seen before, add it to the result and mark it as seen
            result += char#add the character to the result string
            seen.add(char)#mark the character as seen by adding it to the set
    return result #return the result string with duplicates removed
s = "hello world"
print(remove_duplicates(s))
'''tc o(n) where n is the length of the input string, sc o(n) for the seen set and result string in the worst case when all characters are unique'''
