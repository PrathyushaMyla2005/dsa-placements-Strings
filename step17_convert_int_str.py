'''find the integer representation of a string
example1 s= "123" output: "123" because it is the string representation of the input integer
example2 s= "abc" output: None because it cannot be converted to a string representation of an integer
example3 s= "12a3" output: None because it contains non-digit characters and cannot be converted to a string representation of an integer
example4 s= "-123" output: None because it contains a negative sign and cannot be converted to a string representation of an integer'''
def integer_to_string(n):
    if n < 0: #check if the input integer is negative
        return None #if it is negative, return None because it cannot be converted to a string representation of an integer
    return str(n) #convert the integer to a string and return it
n = 123
print(integer_to_string(n))
n = -123
print(integer_to_string(n))
'''tc o(1) for the integer to string conversion process, sc o(n) where n is the number of digits in the input integer for the resulting string representation 
'''