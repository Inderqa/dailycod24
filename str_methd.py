
str = "harry"
german_char = "ß"
print(str.capitalize())
print(str.upper())
print(str.lower()) # >> The casefold() method returns a string where all the characters are lower case.
print(german_char.casefold())
print(str.center(50))   #>>>>> it will move string to center here taking up
                        # the space of 20 characters, with "harry" in the middle

print(str.count("r"))  # >> Returns the number of times a specified value occurs in a string ###

print(str.endswith("yz"))  #Returns true if the string ends with the specified value#
print(str.expandtabs(5))

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
print(txt1)
print(str.strip("a")) # remove leading and trailing whitespace #

# 1. strings are immutable.
# 2. any method on string takes a copy of the object.
# 3.string.upper will convert the string to an upper case
# 4.string.lower will convert the string to lower case
# 5. string.rstrip("character") will strip the trailing characters of string
# 6.string.replace("character/alphabets", new character/alphabets") will replace the existing specified alphabets in string with new ones
# 7. string.split splits the string at the given alphabet and returns a list of items
# 8.string.capitalize capitalizes the first character of the word and turns rest all the characters to lower case
# 9.string.center center aligns the string by adding the number of spaces mentioned in parenthesis
# 10. string.count counts the total number of a particular set of characters in a string
# 11. string.endswith checks whether a string ends with the specific characters
# 12.string.find finds the first occurrence of a given value and return the index value of the position of that occurrence
# 13.string.index finds the occurrence of a given value and returns the index value of the position however, if it is unable to find it will give an error causing the program to exit
# 14.string.isalnum checks to find if string is alphanumeric and returns true or false
# 15.string.isalpha checks if there are any numbers in the string
# 16.string.islower checks if there are only lower aphabets in the string
# 17. string.isprintable checks if all the characters are printable in the string(non printable characters e.g \n)
# 18 string.isspace checks if any space bar has been used in the string
# 19.string.istitle The istitile() returns True only if the first letter of each word of the string is capitalized, else 20. string.isupper checks if all characters are uppercase in a string
# 21. string.startswith checks if a string starts with a given value
# 22. string.swapcase convert uppercase to lowercase and vice versa in a string
# 23.string.title converts first character of all the words in the sentence to capital


