# integer = int(input("Enter number for integer: "))
#
# convert = float(integer)
# print(convert)
# print(type(convert))

 # >>>>> **************************** <<<<<< #
#### String to decimal #####

# import decimal
# str = '123456'
# print(decimal.Decimal(str))
# print(type(decimal.Decimal(str)))

# >>>>> **************************** <<<<<< #

###### STRING REVERS USING LIST AND LOOPS AND USING INBUILT SLICING ########
# string = "Python Programming"
# s =list(string)
# print("List before removing space ",s)
# print(s)
#
# new_lis = [item.strip() for item in s]
# print("List after removing space ",new_lis)
# lst_reverse = []
# for i in new_lis:
#     lst_reverse.append(i[::-1])
# print(lst_reverse)

# >>>>> **************************** <<<<<< #

## Reverse string using loop ##

# str = "Hello World"
# reverse_str = ""
# for i in str:
#     reverse_str = i + reverse_str
# print(reverse_str)

# >>>>> **************************** <<<<<< #

## Reverse string using join ##
# s = "HELLO WORLD"
# reversed_s = ''.join(reversed(s))  # Or s[::-1] for reversing
# print(reversed_s)

# >>>>> **************************** <<<<<< #

### find vowels and consonants in words" ######
# vowel =  ['a','e','i','o','u']
# vowel_in_word =[]
# const_in_word = []
# for i in s:
#     if i in vowel:
#         vowel_in_word.append(i)
#     else:
#         const_in_word.append(i)
# print(vowel_in_word)
# print(const_in_word)
# vowel_string = ' '.join(f"'{v}'"for v in vowel_in_word)
# print(vowel_string)

# >>>>> **************************** <<<<<< #
### Recurrence of character in the word ###
word = 'programming'
char_count={}
for char in word:
    if char in char_count:
        char_count[char]=char_count[char]+1
    else:
        char_count[char]=1
print(char_count)

# >>>>> **************************** <<<<<< #
### Fibonnacci Series using list comprehension###

fib =[0,1]
for i in range(5):
    fib.append(fib[-1]+fib[-2])
str =list((str(e) for e in fib))
print(str)


# >>>>> **************************** <<<<<< #
### Max,Min and middle element in the list###

lst =[5,7,9,8,1,3,50,20,99]
max_num=lst[0]
min_num=lst[0]
for i in range (len(lst)):
    if max_num<lst[i]:
        max_num=lst[i]
    elif min_num>lst[i]:
        min_num=lst[i]
print(f"Max number in List {lst} is = " ,max_num)
print(f"Min number in List {lst} is = ", min_num)

middle_element = int(len(lst)/2)
print("Middle Element: ", lst[middle_element])







