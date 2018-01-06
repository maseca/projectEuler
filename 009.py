import math
magicNum = 1000

def main():
    print(getProduct(magicNum))

def getProduct(magicNum):
    for a in range(1, magicNum):
        for b in range(a+1, magicNum):
            c = math.sqrt(a**2 + b**2)

            if c.is_integer() and a + b + c == magicNum:
                return int(a * b * c)


if __name__ == '__main__': main()