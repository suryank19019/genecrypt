inp = input()
temp = 0
for i in inp:
    i = i.lower()
    if 96 < ord(i) < 123:
        temp = ord(i)-3
        if temp < 97:
            temp = 123 - (97 - temp)
        print(chr(temp).upper(), end="")
    else:
        print(i, end="")
