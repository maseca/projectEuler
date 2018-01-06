# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sumOfSqr = sqrOfSum = 0

for n in range(1, 101):
    sumOfSqr += n**2
    sqrOfSum += n

sqrOfSum **= 2

print(abs(sumOfSqr - sqrOfSum))