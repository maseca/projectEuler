def main():
    nums = []

    for n in range(10001):
        cnd = get_friend(n)
        if cnd is not None:
            nums.append(n)
            nums.append(cnd)

    print(sum(nums))


def p_divs(n):
    divs = [1]
    for i in range(2, n//2 + 1):
        if n % i == 0:
            divs.append(i)

    return divs


def get_friend(n):
    temp = sum(p_divs(n))
    return temp if temp < n and sum(p_divs(temp)) == n else None


if __name__ == '__main__': main()