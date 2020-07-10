"""fibonacci"""


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


j = int(input("Enter the number: "))
if j <= 0:
    print("Please enter a positive number")
else:
    for i in range(j):
        print(fib(i))
