'''find the anagram of the string  
example:s="abcedfg" p = "abc" output: [0,1,2]
'''
def find_anagram(s,p):
    result = []#initialize an empty list to store the result
    if len(p) > len(s):#if the length of p is greater than s then return empty list
        return []
    p_count = [0] * 26 #initialize a list of size 26 to store the count of characters in p
    window_count = [0] * 26 #initialize a list of size 26 to store the count of characters in the current window of s
    for i in range(len(p)): #iterate through the characters in p and update the count in p_count
        p_count[ord(p[i]) - ord('a')] += 1#ord() function returns the ASCII value of the character and we subtract the ASCII value of 'a' to get the index in the list
        window_count[ord(s[i])- ord('a')] += 1#update the count in window_count for the first window of s
        if p_count == window_count:#if the count of characters in p is equal to the count of characters in the current window of s then we found an anagram
            result.append(0)#append the starting index of the anagram to the result list
        for i in range(len(p), len(s)):#iterate through the remaining characters in s
            window_count[ord(s[i]) - ord('a')] += 1#update the count in window_count for the new character added to the window
            window_count[ord(s[i - len(p)]) - ord('a')] -= 1#update the count in window_count for the character removed from the window
            if p_count == window_count:#if the count of characters in p is equal to the count of characters in the current window of s then we found an anagram
                result.append(i - len(p) + 1)#append the starting index of the anagram to the result list
    return result#return the result list
s = "abcedfg"
p = "abc"
print(find_anagram(s,p))
'''tc:O(n) where n is the length of the string s
sc:O(1) because we are using a fixed size list of size 26 to store the count of characters in p and the current window of s'''