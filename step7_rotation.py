'''find the rotation string for one string to become another string
example1 s= abcde, goal= cdeab becomes true
example2 s= abcde, goal= abced becomes false'''
def rotate_String(s,goal):
    if len(s) != len(goal): #if lengths are different, they cannot be rotations of each other
        return False
    return goal in s + s #check if goal is a substring of s concatenated with itself
s = "abcde"
goal = "cdeab"
print(rotate_String(s,goal))
s = "abcde"
goal = "abced"
print(rotate_String(s,goal))
'''tc o(n) where n is length of input strings, sc o(n) for concatenated string s+s'''