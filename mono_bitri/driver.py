from monoalpha import *
import os

def parse(st):
    parsed_list = []
    cur = ""
    for i in st:
        if i == '[':
            cur = ""
        elif i == ']':
            parsed_list.append(cur)
        else:
            cur += i
    return parsed_list


cipher_file = os.path.join("E:\IIITD\Semester 1\AI\Project", "cipher.txt")
cipher_file = open(cipher_file)
cipher = cipher_file.read()

res_file = os.path.join("E:\IIITD\Semester 1\AI\Project", "result.txt")
res_file = open(res_file)
results = res_file.read()

print(cipher)
ciphers = parse(cipher)
results = parse(results)

plain_texts = []
for cur_cipher in ciphers:
    print ("Current Cipher = ", cur_cipher)
    mono = Mono([], cur_cipher)
    mono.add_pop(mono.initialize(pop_limit))
    mono.print_pop()
    mono.genetic()
    cur_best = mono.get_last()
    plain_texts.append(cur_best[2])

acc = 0
for i in range(len(plain_texts)):
    print("["+plain_texts[i]+"]")
    print(results[i])
    if plain_texts[i] == results[i]:
        acc += 1
        print("MATCHED")

print("accuracy = ", acc/len(results) * 100)
