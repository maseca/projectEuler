# Which starting number, under one million, produces the longest chain? (Collatz Sequence)

def main():
    max = result = 0

    for n in range(1000000):
        candidate = collatz(n)
        if candidate > max:
            max = candidate
            result = n

    print(result)


def collatz(n, i=None):
    if i is None:
        i = 1
    if n is 1 or n is 0:
        return i

    if i is not None:
        i += 1

    if n % 2 is 0:
        n = n // 2
    else:
        n = 3*n + 1

    return collatz(n, i)


if __name__ == '__main__': main()
