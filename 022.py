import re


def main():
    file = open("p022_names.txt")

    names = []
    for line in file:
        names = sorted(re.sub('"', '', line).split(','))

    scores = []
    for n in range(len(names)):
        scores.append(score(names[n]) * (n+1))

    print(sum(scores))


def score(name):
    out = 0
    for char in name:
        out += ord(char) - 64

    return out


if __name__ == '__main__': main()