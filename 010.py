# Find the sum of all the primes below two million.
import math

def main():
    sum, max, primes = 0, 2000000, []

    for n in range(0, max):
        if isPrime(n):
            primes.append(n)

    for n in primes:
        sum += n

    print(sum)


def isPrime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = math.floor(math.sqrt(n))
        for x in range(5, int(r+1), 6):
            if n % x == 0 or n % (x+2) == 0:
                return False
        return True


if __name__ == '__main__': main()
