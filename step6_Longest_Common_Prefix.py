'''find the largest common prefix string amongst an array of strings
example1 ["flower","flow","flight"] becomes "fl"
example2 ["dog","racecar","car"] becomes ""
example3 ["interspecies","interstellar","interstate"] becomes "inters"'''
def longest_prefix(str): 
    if not str: # if input list is empty, return empty string
        return ""
    str.sort() # sort the list of strings
    first = str[0] # get the first string (smallest lexicographically)
    last = str[-1] # get the last string (largest lexicographically)
    i = 0 # index to compare characters
    while i < len(first) and  i < len(last) and first[i] == last[i]:# compare characters of first and last string
        i += 1 # move to next character
    return first[:i] # return the common prefix (substring of first string up to index i)
str = ["flower","flow","flight"]
print(longest_prefix(str))
'''tc o(n log n) for sorting the list of strings, sc o(1) for variables used in the function
Note: the sorting step dominates the time complexity, and the space complexity is constant since we are only using a few variables to store intermediate results.'''