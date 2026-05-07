'''frequency of words in the text
example:banana:b= 1,a=3,n=2'''
def frequency_words(text):
    fre = {} #initialize an empty dictionary to store the frequency of each word
    for ch in text: #iterate through each character in the input text
        if ch in fre: #if the character is already in the frequency dictionary, increment its count
            fre[ch] += 1
        else: #if the character is not in the frequency dictionary, add it with a count of 1
            fre[ch] = 1
    return fre #return the frequency dictionary
text = "banana"
print(frequency_words(text))
'''tc o(n) where n is the length of the input text, sc o(m) where m is the number of unique characters in the text'''   
