import time
# from fitness import fit_bi_check
import random
import operator
from ngram_score import ngram_score


class Mono:

    def __init__(self, KS, C):
        self.keyspace = KS
        self.cipher = C

    def add_pop(self, orderings):
        for key in orderings:
            # count, res = fit_bi_check(key)
            deciphered = self.convert(key)
            score = round(fitness.score(deciphered), 2)
            self.keyspace.append((key, score, deciphered))

    def print_pop(self):
        for x in self.keyspace:
            print(x)

    def get_last(self):
        return self.keyspace[len(self.keyspace)-1]

    def sorter(self):
        self.keyspace.sort(key=operator.itemgetter(1))

    def selectBest(self):
        self.keyspace = self.keyspace[-top_select:]
        # self.keyspace = self.keyspace[:top_select]


    def initialize(self, total):
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


    def hill_climb(self):
        for tup in self.keyspace:
            i = random.randrange(0, 26)
            j = random.randrange(0, 26)
            tmp = list(tup[0])
            tmp[i], tmp[j] = tmp[j], tmp[i]
            deciphered = self.convert(tmp)
            score = round(fitness.score(deciphered), 2)
            if score > tup[1]:
                self.keyspace.append((tuple(tmp), score, deciphered))
                # print(" climbed ", end="")
                self.keyspace.remove(tup)
            # else:
            #     print(" didn't climb ", end="")

    def genetic(self):
        global generations
        cur_gen = 0
        while generations > cur_gen:
            if cur_gen % r_offspring_lim == r_offspring_lim - 1:  # random offspring generation
                print("random offspring generation")
                self.add_pop(self.initialize(pop_limit - top_select))
            else:
                orderings = set()
                for i in range(0, pop_limit - top_select):
                    rankey = random.randint(0, top_select - 1)
                    parent1 = self.keyspace[rankey][0]
                    child = list(parent1)
                    a = random.randrange(0, 26)
                    b = random.randrange(0, 26)
                    child[a], child[b] = child[b], child[a]
                    deciphered = self.convert(child)
                    score = round(fitness.score(deciphered), 2)
                    if score > self.keyspace[rankey][1]:
                        self.keyspace[rankey] = (tuple(child), score, deciphered)
                    orderings.add(tuple(child))
                self.add_pop(orderings)
            print("generation= ", cur_gen)
            self.hill_climb()
            self.sorter()
            self.selectBest()
            self.print_pop()
            cur_gen = cur_gen + 1
            # generations = generations + 1
            print("//////////////////////////////////////////////////////////////////////////////////////////////")


    def convert(self, key):
        str = ""
        for w in self.cipher:
            for i in range(0, len(w)):
                for j in range(0, len(key)):
                    if w[i] == key[j]:
                        w = w[:i] + chr(j + 65) + w[i + 1:]
                        break
            # res.append(w)
            str += w
        return str


pop_limit = 100
generations = 250
top_select = 70
mut_prob = 0.2
r_offspring_lim = 30
biasing_value = 2
fitness = ngram_score("E:\IIITD\Semester 1\AI\Project\english_quadgrams.txt")
