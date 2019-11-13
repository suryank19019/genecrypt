import os
import random

path = "E:\IIITD\Semester 1\AI\Project"
pt_file = os.path.join(path, "plainText.txt")
plainText = open(pt_file).read()
print(plainText)

key = ['A'] * 26
for i in range(len(key)):
    key[i] = chr(i+65)
random.shuffle(key)
print(key)

res = ""
for i in plainText:
    i = i.upper()
    if i == ']':
        res += "]\n"
    elif i != ' ' and i != '\n':
        res += i
res_file = os.path.join(path, "result.txt")
result = open(res_file, "w")
result.write(res)


res = ""
i_res = ""
for i in plainText:
    temp = ""
    i = i.lower()
    if i == '[':
        i_res = ""
    elif 96 < ord(i) < 123:
        temp = key[ord(i) - 97]
    elif i == ']':
        res += "[" + i_res + "]\n"
    elif i != ' ' and i != '\n':
        temp = i
    i_res += temp

print(res)
cipher_file = os.path.join(path, "cipher.txt")
cipher = open(cipher_file, "w")
cipher.write(res)
