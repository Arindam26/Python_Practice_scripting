"""Prime or not """


# def prime(n):
#     if n > 1:
#         for i in range(2, n):
#             if n % i == 0:
#                 print("{} is not a prime".format(n))
#                 break
#
#         else:
#             print("{} is a prime".format(n))
#
#
# a = int(input("Please enter a number to check , if prime or not : "))
# prime(a)


def prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                print("{} is not a prime".format(n))
                break
        else:
            print("{} is a prime.".format(n))

    else:
        print("Please enter a positive number ")


a = int(input("Enter a number to check if prime or not: "))
prime(a)
