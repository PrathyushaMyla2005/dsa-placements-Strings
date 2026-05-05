'''count the number of vowels in a string
example "hello" has 2 vowels (e and o)
"world" has 1 vowel (o)
'''
def count_vowels(s):#define a function that takes a string as input
    count = 0 #initialize a counter to 0
    for char in s:
        if char.lower() in "aeiou":
            count += 1
    return count
s = "hello"
print(count_vowels(s))
s = "world"
print(count_vowels(s))
'''tc o(n) where n is length of input string, sc o(1) for count variable'''