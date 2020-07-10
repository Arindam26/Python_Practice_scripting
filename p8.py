"""PRIME"""


def prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                print(n, " is not a prime number")
                break
        else:
            print(n, " is a prime  number")


a = int(input("Please enter a number to check prime or not: "))
prime(a)
