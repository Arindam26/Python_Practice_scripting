# def palindrom(w):
#     return w == w[::-1]
#
#
# w = input()
# result = palindrom(w)
#
# if result:
#     print("{} is palindrome".format(w))
# else:
#     print("{} is not a palindrome".format(w))
#


"""Palindrome function """


def palindrome(w):
    return w == w[::-1]


string = input("Please enter the string to check if palindrome or not! : ")
result = palindrome(string)

if result:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
