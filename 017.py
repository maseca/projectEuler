# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

ones = {
    0: 0, #None,
    1: 3, #"one",
    2: 3, #"two",
    3: 5, #"three",
    4: 4, #"four",
    5: 4, #"five",
    6: 3, #"six",
    7: 5, #"seven",
    8: 5, #"eight",
    9: 4, #"nine"
} #sum == 36

teens = {
    10: 3, #"ten",
    11: 6, #"eleven",
    12: 6, #"twelve",
    13: 8, #"thirteen",
    14: 8, #"fourteen",
    15: 7, #"fifteen",
    16: 7, #"sixteen",
    17: 9, #"seventeen",
    18: 8, #"eighteen",
    19: 8, #"nineteen"
} #sum == 70

tens = {
    20: 6, #"twenty",
    30: 6, #"thirty",
    40: 5, #"forty",
    50: 5, #"fifty",
    60: 5, #"sixty",
    70: 7, #"seventy",
    80: 6, #"eighty",
    90: 6, #"ninety"
} #sum == 46

#100: 10(13), "one hundred (and)"
#1000: 11, "one thousand"

def gen99():
    pass
