# Find the largest palindrome made from the product of two 3-digit numbers.

def main():
    i, j, out, pals = 999, 999, 0, []

    for i in range(1, 1000):
        for j in range(1, 1000):
            if isPalindrome(str(i * j)):
                pals.append(i * j)

    for p in pals:
        if p > out:
            out = p

    print(out)


def isPalindrome(str):
    pvt = len(str) // 2

    if len(str) % 2 != 0:
        return str[:pvt] == str[:pvt:-1]
    else:
        return str[:pvt] == str[:pvt-1:-1]


if __name__ == "__main__" : main()
