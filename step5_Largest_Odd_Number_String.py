'''find the largest odd number in a string of digits
example1 "52" becomes "5"
example2 "4206" becomes "420"
example3 "731" becomes "731"
example4 "13579" becomes "13579"'''
def largest_odd_number(s): # function takes string s as input
    result = ""         # store final answer (empty at start)

    for char in s:      # go through each character in string

        if int(char) % 2 == 1:  # if current character is odd

            result += char       # add it to result

    return result           # return final string
s = "52"
print(largest_odd_number(s))
s = "4206"
print(largest_odd_number(s))
s = "731"
print(largest_odd_number(s))
s = "13579"
print(largest_odd_number(s))
'''tc o(n) where n is length of input string, sc o(n) for result string in worst case (all odd digits)'''