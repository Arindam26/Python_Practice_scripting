# """fibonacci"""
#
#
# def fib(n):
#     if n <= 1:
#         return n
#
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# j = int(input("Enter a number to check the fibonacci series : "))
# if j <= 0:
#     print("Please enter  a positive number ")
# else:
#     for i in range(j):
#         print(fib(i))

"""fibonacci"""


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


j = int(input("Input a number to print the fibonacci series : "))
if j < 0:
    print("Please pass  a positive number!")

else:
    for i in range(j):
        print(fib(i))
