'''
Exercise 4: Remove first n characters from a string
Write a program to remove characters from a string starting from zero up to n and return a new string.
For example:
remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a string.
remove_chars("pynative", 2) so output must be native. Here we need to remove first two characters from a string.
Note: n must be less than the length of the string.'''

str = input("Enter any word: ")
print(f"Original String: {str}")
str_length = len(str)
number = int(input("Enter a number to trim the string: "))
if number <= str_length:
    new_str = str[number:]
    print(f"After trimming: {new_str}")
else:
    print(f"Entered trim value is greater than the string length")
