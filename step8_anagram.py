'''check if two strings are anagrams of each other
example1 s= "listen", t= "silent" becomes true
example2 s= "hello", t= "world" becomes false'''
def is_anagram(s,t):
    if len(s) != len(t):
        return False
    if sorted(s) == sorted(t):
        return True
    return False
s = "listen"
t = "silent"
print(is_anagram(s,t))
s = "hello"
t = "world"
'''tc o(n log n) for sorting both strings, sc o(n) for sorted lists of characters
Note: the sorting step dominates the time complexity, and the space complexity is linear since we are creating sorted lists of characters from the input strings.'''
#optimized solution using character count
def is_anagram(s,t):
    if len(s) != len(t):#if lengths are different, they cannot be anagrams
        return False
    freq = 0 * 26 #initialize a frequency array of size 26 for lowercase letters
    for char in s:
        freq[ord(char) - ord('a')] += 1 #increment the frequency count for characters in s
    for char in t:
        freq[ord(char) - ord('a')] -= 1 #decrement the frequency count for characters in t
    for count in freq:
        if count != 0: #if any count is not zero, then s and t are not anagrams
            return False
    return True #if all counts are zero, then s and t are anagrams
s = "listen"
t = "silent"
print(is_anagram(s,t))
s = "hello"
t = "world"
print(is_anagram(s,t))
'''tc o(n) where n is length of input strings, sc o(1) for frequency array of fixed size 26
'''