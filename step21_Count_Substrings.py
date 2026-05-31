'''count the number of substrings in a string
example: "abc" has 6 substrings: "a", "b", "c", "ab", "bc", "abc"'''
def count_substrings(s):
    count =  0 # initialize count to 0
    n = len(s) # get the length of the string
    for i in range(n): # loop through the string
        for j in range(i,n): # loop through the string again
            count += 1 # increment count for each substring
    return count # return the final count
example = "abc"
print(count_substrings(example)) # Output: 6
'''tc: O(n^2) because we have two nested loops, sc: O(1) because we are using a constant amount of space
to store the count'''
