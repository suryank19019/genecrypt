import time
# import enchant
import os


def init():
    global setup, words, cipher
    file = os.path.join(path, "corncob_caps.txt")
    cipher_file = os.path.join(path, "cipher.txt")
    my_file = open(file)
    words = my_file.read().split()
    my_cipher_file = open(cipher_file)
    cipher = my_cipher_file.read().split()
    #print(words)
    print(cipher)
    setup = True


def check_word(w):
    return w in words


def fit_word_check(key):
    if not setup:
        init()
    start_time = time.time()
    count = 0
    # d = enchant.Dict("en_US")
    # print(words)
    res = []
    for w in cipher:
        for i in range(0, len(w)):
            for j in range(0, len(key)):
                if w[i] == key[j]:
                    w = w[:i] + chr(j + 65) + w[i + 1:]
                    break
        res.append(w)
        # if d.check(w):
        if check_word(w):
            count += 1
    end_time = time.time() - start_time
    if count == len(cipher):
        print("ANSWER FOUND")
        print(key)
        print(res)
        exit(0)
    return count, res


setup = False
path = "E:\IIITD\Semester 1\AI\Project"
cipher_file = "cipher.txt"
cipher = []
words = []
'''
xyz = ('X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
      'R', 'S', 'T', 'U', 'V', 'W')
a, b = fit_word_check(xyz)
print(a, b)
'''
# the quick brown fox jumps over the lazy dog
# qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald

# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# X Y Z A B C D E F G H I J K L M N O P Q R S T U V W

'''
I will be honest with you for now lying would be the second worst thing I could do at the moment I am talking to you
 in the hopes that a fraction of my consciousness may get diverted elsewhere and the monstrosity that is feeding off
  my left leg gets weakened This is not good I thought about him again I cannot tell at this point if moving my leg
   would be a good idea or not It is as if you are hanging holding a barbed wire and there are bear traps on the ground
    and every time you think about one or the other one of them gets closer to killing you I keep glancing towards my
     leg I can almost see him now That is never a good sign Damn it I have already given him the acknowledgement that
      he subsists We have burnt the bridge of ignoring him I must take some action lest my soul be dragged with his
      The quick brown fox jumps over the lazy dog
'''

'''
F TFII YB ELKBPQ TFQE VLR CLO KLT IVFKD TLRIA YB QEB PBZLKA TLOPQ QEFKD F ZLRIA AL XQ QEB JLJBKQ F XJ QXIHFKD QL VLR FK
 QEB ELMBP QEXQ X COXZQFLK LC JV ZLKPZFLRPKBPP JXV DBQ AFSBOQBA BIPBTEBOB XKA QEB JLKPQOLPFQV QEXQ FP CBBAFKD LCC JV
  IBCQ IBD DBQP TBXHBKBA QEFP FP KLQ DLLA F QELRDEQ XYLRQ EFJ XDXFK F ZXKKLQ QBII XQ QEFP MLFKQ FC JLSFKD JV IBD TLRIA
   YB X DLLA FABX LO KLQ FQ FP XP FC VLR XOB EXKDFKD ELIAFKD X YXOYBA TFOB XKA QEBOB XOB YBXO QOXMP LK QEB DOLRKA XKA
    BSBOV QFJB VLR QEFKH XYLRQ LKB LO QEB LQEBO LKB LC QEBJ DBQP ZILPBO QL HFIIFKD VLR F HBBM DIXKZFKD QLTXOAP JV IBD
     F ZXK XIJLPQ PBB EFJ KLT QEXQ FP KBSBO X DLLA PFDK AXJK FQ F EXSB XIOBXAV DFSBK EFJ QEB XZHKLTIBADBJBKQ QEXQ EB
      PRYPFPQP TB EXSB YROKQ QEB YOFADB LC FDKLOFKD EFJ F JRPQ QXHB PLJB XZQFLK IBPQ JV PLRI YB AOXDDBA TFQE EFP
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