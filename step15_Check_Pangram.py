'''find the pangram in a string
a pangram is a sentence that contains every letter of the alphabet at least once
example1 s= "the quick brown fox jumps over the lazy dog" output: True because it contains every letter of the alphabet at least once
example2 s= "hello world" output: False because it does not contain every letter of
the alphabet at least once
'''
def is_pangram(s):
    s =s.lower() #convert the input string to lowercase to ignore case sensitivity
    letters = set() #initialize an empty set to keep track of unique letters in the string
    for char in s: #iterate through each character in the input string
        if char.isalpha(): #if the character is an alphabet letter, add it to the set
            letters.add(char) #add the character to the set of letters
    return len(letters) == 26 #return True if the number of unique letters is   
#equal to 26 (the number of letters in the English alphabet), otherwise return False
s = "the quick brown fox jumps over the lazy dog"
print(is_pangram(s))
s = "hello world"
print(is_pangram(s))
'''tc o(n) where n is the length of the input string, sc o(m) where m is the number of unique letters in the input string for the letters set, which is at most 26 for the English alphabet'''
