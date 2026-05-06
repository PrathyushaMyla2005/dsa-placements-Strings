'''find the valid palindrome in a string, ignore the non-alphanumeric characters and case sensitivity
example1 s= "A man, a plan, a canal: Panama" becomes true
example2 s= "race a car" becomes false
'''
def is_palindrome(s):
    result = " " #initialize an empty list to store alphanumeric characters
    for char in s: #iterate through each character in the input string
        if char.isalnum(): #check if the character is alphanumeric
          result += char.lower() #if it is, convert it to lowercase and add it to the result string
    return result == result[::-1] #check if the result string is equal to its reverse
s = "A man, a plan, a canal: Panama"
print(is_palindrome(s))
s = "race a car"
print(is_palindrome(s))
'''tc o(n) where n is the length of the input string, sc o(n) for the result string that stores the alphanumeric characters'''