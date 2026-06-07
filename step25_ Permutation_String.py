'''find the permutation of the string
example:s="abc" p = "bca" output: True
'''
def is_permutation(s,p):
    if len(s) > len(p):#if the length of s is greater than p then return False
        return False
    s_count = [0] * 26 #initialize a list of size 26 to store the count of characters in s
    p_count = [0] * 26 #initialize a list of size 26 to store the count of characters in p
    for i in range(len(s)):#iterate through the characters in s and update the count in s_count
        s_count[ord(s[i]) - ord('a')] += 1#ord() function returns the ASCII value of the character and we subtract the ASCII value of 'a' to get the index in the list
        p_count[ord(p[i]) - ord('a')] += 1#update the count in p_count for the first window of p
    if s_count == p_count:#if the count of characters in s is equal to the count of characters in p then we found a permutation
        return True
    for i in range(len(s), len(p)):#iterate through the remaining characters in p
        p_count[ord(p[i]) - ord('a')] += 1#update the count in p_count for the new character added to the window
        p_count[ord(p[i - len(s)]) - ord('a')] -= 1#update the count in p_count for the character removed from the window
        if s_count == p_count:#if the count of characters in s is equal to the count of characters in the current window of p then we found a permutation
            return True
    return False#return False if we did not find any permutation
s = "abc"
p = "bca"
print(is_permutation(s,p))
'''tc:O(n) where n is the length of the string p
sc:O(1) because we are using a fixed size list of size 26 to
store the count of characters in s and p'''