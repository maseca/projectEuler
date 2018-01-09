# What is the value of the first triangle number to have over five hundred divisors?
from math import sqrt
from numpy import unique

def main():
    out = []
    i = sum = 0

    while len(unique(out)) < 501:
        i += 1
        sum += i
        out = []
        for n in list(factors(sum)):
            out += n

    print(sum, unique(out))


def factors(n):
    for i in range (1, int(sqrt(n)) + 1):
        if n % i == 0:
            yield [i, n//i]


if __name__ == '__main__': main()