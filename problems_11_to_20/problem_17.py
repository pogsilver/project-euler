def num_in_words_len(num):
    """returns the length of the number in words.
    The number is between 1 and 1000

    Args:
        num (int): the number to calculate its length in words. should be between 1 and 999
    Returns:
        int: the length of the number in words
    """

    if num < 1 or 999 < num:
        return -1

    units = num % 10
    tens = (num % 100) // 10
    hundreds = num // 100
    s = 0
    if hundreds > 0:
        s += len_dic[hundreds] + len("hundred")
        if tens > 0 or units > 0:
            s += len("and")
    if tens > 1:
        s += len_dic[tens * 10] + len_dic[units]
    elif tens == 1:
        s += len_dic[10 * tens + units]
    else:
        s += len_dic[units]

    return s

digits_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens_words = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens_words = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

len_dic = {0: 0}
for i, word in enumerate(digits_words):
    len_dic[i + 1] = len(word)

for i, word in enumerate(teens_words):
    len_dic[i + 11] = len(word)

for i, word in enumerate(tens_words):
    len_dic[10 * (i + 1)] = len(word)

s = len("one thousand") - len(" ")

for i in range(1, 1000):
    s += num_in_words_len(i)

print(s)

