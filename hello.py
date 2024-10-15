# a=float(input("Enter first number: "))
# b=float(input("Enter second number: "))
# c = a + b
#
# print(f"Sum of 2 nos. is = {c} ")

n=int(input("Enter first number: "))

def factorial(n):
    if n==0 or n ==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(n))