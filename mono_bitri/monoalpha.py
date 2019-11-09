import time
# from fitness import fit_bi_check
import random
import operator
import os
from ngram_score import ngram_score


class Keystore:

    def __init__(self):
        self.keyspace = []

    def add_pop(self, orderings):
        for key in orderings:
            # count, res = fit_bi_check(key)
            deciphered = convert(key)
            score = fitness.score(deciphered)
            self.keyspace.append((key, score, deciphered))

    def print_pop(self):
        for x in self.keyspace:
            print(x)

    def sorter(self):
        self.keyspace.sort(key=operator.itemgetter(1))

    def selectBest(self):
        self.keyspace = self.keyspace[-top_select:]
        # self.keyspace = self.keyspace[:top_select]


def initialize(total):
    key = [0] * 26
    orderings = set()
    while total > 0:
        order = [0] * 26
        for i in range(0, 26):
            order[i] = chr(i+65)
        random.shuffle(order)
        orderings.add(tuple(order))
        total = total - 1
    print("initialized")
    return orderings

'''
def hillclimb():
    for tup in keystore.keyspace:
        flag = True
        comp_lim = tup[1]
       # while flag:
        i = random.randrange(0, 26)
        tmp = list(tup[0])
        pos = random.randrange(0, 26)
        med = tmp[i]
        tmp[i] = tmp[pos]
        tmp[pos] = med
        wc, wl = fit_bi_check(tmp)
    #    if wc > comp_lim:
        flag = False
        keystore.keyspace.append((tuple(tmp), wc, wl))
        comp_lim = wc
        # print("climbed", end="")
        keystore.keyspace.remove(tup)
'''


def genetic():
    global generations
    curgen = 0
    while generations > curgen:
        keystore.sorter()
        # hillclimb()
        keystore.selectBest()
        keystore.print_pop()
        print("generation= ", curgen)
        if curgen % r_offspring_lim == r_offspring_lim - 1:  # random offspring generation
            print("random offspring generation")
            keystore.add_pop(initialize(pop_limit - top_select))
        else:
            orderings = set()
            for i in range(0, pop_limit - top_select):
                rankey = random.randint(0, top_select - 1)
                parent1 = keystore.keyspace[rankey][0]
                child = list(parent1)
                a = random.randrange(0, 26)
                b = random.randrange(0, 26)
                child[a], child[b] = child[b], child[a]
                deciphered = convert(child)
                score = fitness.score(deciphered)
                if score > keystore.keyspace[rankey][1]:
                    keystore.keyspace[rankey] = (tuple(child), score, deciphered)
                '''
                print(parent1, ranpos1)
                print(parent2, ranpos2)

                print(undone)
                print(child, len(child))
                print()
                '''
                orderings.add(tuple(child))
            keystore.add_pop(orderings)
        curgen = curgen + 1
        generations = generations + 1
        print("//////////////////////////////////////////////////////////////////////////////////////////////")


def convert(key):
    # res = []
    str = ""
    for w in cipher:
        for i in range(0, len(w)):
            for j in range(0, len(key)):
                if w[i] == key[j]:
                    w = w[:i] + chr(j + 65) + w[i + 1:]
                    break
        # res.append(w)
        str += w
    return str


pop_limit = 100
generations = 10
top_select = 70
mut_prob = 0.2
r_offspring_lim = 30
biasing_value = 2
fitness = ngram_score("E:\IIITD\Semester 1\AI\Project\english_quadgrams.txt")
cipher_file = os.path.join("E:\IIITD\Semester 1\AI\Project", "cipher.txt")
my_cipher_file = open(cipher_file)
cipher = my_cipher_file.read()
start_time = time.time()
keystore = Keystore()
keystore.add_pop(initialize(pop_limit))
keystore.print_pop()
genetic()
