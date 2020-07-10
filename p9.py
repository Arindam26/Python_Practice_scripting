"""Palindrome"""

n = input("Enter a number: ")
b = n[::-1]
if n == b:
    print(n, "is palindrome")

else:
    print("It's a natural number")
