# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?


def main():
    Fp, Fc, index = 89, 144, 12

    while len(str(Fc)) < 1000:
        tmp = Fc + Fp
        Fp = Fc
        Fc = tmp
        index += 1

    print(index)


if __name__ == '__main__':
    main()