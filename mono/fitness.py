import time
import os


def prepare_frequencies():
    global frequencies, expected_frequencies
    frequency_file = os.path.join(path, "frequencies.txt")
    my_freq_file = open(frequency_file)
    frequencies = my_freq_file.read().split()
    expected_frequencies = [0] * len(frequencies)
    for i in range(0, len(frequencies)):
        expected_frequencies[i] = (float(frequencies[i]) / 10 * len(cipher))
    print(frequencies)


def prepare_dictionary():
    global words
    file = os.path.join(path, "corncob_caps.txt")
    my_file = open(file)
    words = my_file.read().split()


def init():
    global setup, cipher
    cipher_file = os.path.join(path, "cipher1.txt")
    my_cipher_file = open(cipher_file)
    cipher = my_cipher_file.read().split()
    # prepare_dictionary()
    prepare_frequencies()
    print("Cipher= ", cipher)
    setup = True


def check_word(w):
    return w in words


def convert(key):
    res = []
    for w in cipher:
        for i in range(0, len(w)):
            for j in range(0, len(key)):
                if w[i] == key[j]:
                    w = w[:i] + chr(j + 65) + w[i + 1:]
                    break
        res.append(w)
    return res


def fit_word_check(key):
    if not setup:
        init()
    plain_text = convert(key)
    count = 0
    for word in plain_text:
        if check_word(word):
            count += 1
    if count == len(cipher):
        print("ANSWER FOUND")
        print(key)
        print(plain_text)
        exit(0)
    return count, plain_text


def fit_freq_check(key):
    if not setup:
        init()
    plain_text = convert(key)
    # print("plain_text= ", plain_text)
    count = [0] * len(expected_frequencies)
    for word in plain_text:
        for i in range(len(word)):
            count[ord(word[i])-65] += 1
    error = 0
    for i in range(0, len(expected_frequencies)):
        error += (expected_frequencies[i]-count[i]) ** 2
    return error, plain_text


setup = False
cipher = []
words = []
frequencies = []
expected_frequencies = []
path = "E:\IIITD\Semester 1\AI\Project"
'''
xyz = ('X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
      'R', 'S', 'T', 'U', 'V', 'W')
a, b = fit_word_check(xyz)
print(a, b)
'''


'''
inp = input()
temp = 0
for i in inp:
    i = i.lower()
    if ord(i)>96 and ord(i)<123:
        temp = ord(i)-3
        if temp < 97:
            temp = 123 - (97 - temp) 
            print(chr(temp).upper(), end="")
    else:
        print(i, end="")
'''