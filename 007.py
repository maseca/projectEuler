# What is the 10 001st prime number?

def main():
    i, primes = 29, [2,3,5,7,11,13,17,19,23]

    while len(primes) < 10001:
        if isPrime(i) and i not in primes:
            primes.append(i)
        i += 2

    print(primes[-1])


def isPrime(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True


if __name__ == '__main__': main()
