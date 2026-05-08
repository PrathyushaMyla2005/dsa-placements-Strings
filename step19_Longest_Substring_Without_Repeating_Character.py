'''fibd the length of the longest substring without repeating characters in a given string.
Example 1:
Input: s = "abcabcbb"
Output: 3'''
def length_of_longest_substring(s):
    char_set = set() #create an empty set to store unique characters
    left = 0 #initialize the left pointer of the sliding window
    max_length = 0 #initialize the variable to keep track of the maximum length of substring found

    for right in range(len(s)): #iterate through the string using the right pointer
        while s[right] in char_set: #if the character at the right pointer is already in the set, it means we have a repeating character
            char_set.remove(s[left]) #remove the character at the left pointer from the set
            left += 1 #move the left pointer to the right
        char_set.add(s[right]) #add the current character at the right pointer to the set
        max_length = max(max_length, right - left + 1) #update the maximum length if the current window is larger

    return max_length #return the maximum length of substring without repeating characters
s = "abcabcbb"
print(length_of_longest_substring(s)) #output: 3
'''tc o(n) because we traverse the string once with the right pointer and the left pointer moves at most n times, sc o(min(m,n)) where m is the size of the character set and n is the length of the string, because in the worst case we may have to store all unique characters in the set'''
