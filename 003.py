# What is the largest prime factor of the number 600851475143 ?

def main():
    print(primeFactors(600851475143)[-1])

def primeFactors(num):
    if num <= 0:
        print("Number must be positive.")
        return []
    elif num == 1:
        print("One is the unit number.")
        return []
    else:
        val, factors, i = num, [], 2
        while val > 1:
            if val % i == 0:
                val /= i
                factors.append(i)
            else:
                i += 1
        return factors

if __name__ == "__main__": main()