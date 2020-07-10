from fractions import Fraction
from functools import reduce


def product(fracs):
    t = reduce(lambda x, y: x * y, fracs)
    return t.numerator, t.denominator


if __name__ == '__main__':
    hello = []
    for _ in range(int(input())):
        hello.append(Fraction(*map(int, input().split())))
    result = product(hello)
    print(*result)
