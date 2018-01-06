# By considering the terms in the Fibonacci
# sequence whose values do not exceed four million,
# find the sum of the even-valued terms.
a = sum = 0
b = 1

while(b < 4000000):
    a,b = b,a+b
    if a % 2 == 0:
        sum += a

print(sum)