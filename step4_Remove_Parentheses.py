'''remove parentheses from a string
example1 "((()))" becomes "()"
example2 "(()())" becomes "()()"'''
def remove_parentheses(s):  # function takes string s as input
    result = ""             # store final answer (empty at start)
    open_count = 0          # counts how many '(' are open

    for char in s:          # go through each character in string

        if char == "(":     # if current character is '('

            if open_count > 0:   # if we are already inside (not outer)
                result += char   # add '(' to result

            open_count += 1      # increase count of open brackets

        else:  # char == ')'     # if current character is ')'

            open_count -= 1      # decrease count (closing bracket)

            if open_count > 0:   # if still inside (not outer)
                result += char   # add ')' to result

    return result           # return final string
s = "((()))"
print(remove_parentheses(s))
s = "(()())"
print(remove_parentheses(s))
