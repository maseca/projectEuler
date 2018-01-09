# Find the smallest prime which, by replacing part of the number (not necessarily
# adjacent digits) with the same digit, is part of an eight prime value family.
from Crypto.Util.number import isPrime

def main():
    maxPrimes = first = 0
    n = 99999

    while maxPrimes < 8:
        n += 1
        if not isPrime(n):
            continue

        length = len(str(n))
        for i in range(1, 2**length):
            temp, tempFir = checkDigits(n, format(i, "0"+str(length)+"b"))
            if temp > maxPrimes:
                maxPrimes = temp
                first = tempFir

    print(maxPrimes, first)


def checkDigits(num, mask):
    num = str(num)
    length = len(num)
    mask = str(mask)
    i = numPrimes = 0
    fmt = ""

    while i < length:
        if mask[i] == "1":
            fmt += "*"
        else:
            fmt += num[i]
        i += 1

    x = 1 if fmt[0] == "*" else 0
    for n in range(x, 10):
        if isPrime(int(fmt.replace("*", str(n)))):
            numPrimes += 1

    return numPrimes, fmt.replace("*", str(x))


if __name__ == '__main__': main()