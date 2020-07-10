"""Fibonacci series with lambda """

# from functools import reduce
#
# # fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])
# fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])
#
# for i in range(20):
#     print("Fibonacci series upto {}".format(i))
#     print(fib_series(i))
from functools import reduce

fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])

n = int(input("Please enter a number to see the fib series: "))
for i in range(n + 1):
    print("Fib series upto {}".format(i))
    print(fib_series(i))
