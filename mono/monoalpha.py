import time
from fitness import fit_one
import random
import operator


class Keystore:

    def __init__(self):
        self.keyspace = []

    def add_pop(self, orderings):
        for key in orderings:
            count, res = fit_one(key)
            self.keyspace.append((key, count, res))

    def print_pop(self):
        for x in self.keyspace:
            print(x)

    def sorter(self):
        self.keyspace.sort(key=operator.itemgetter(1))

    def selectBest(self):
        self.keyspace = self.keyspace[-top_select:]


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


def genetic():
    global generations
    curgen = 0
    while generations > curgen:
        keystore.sorter()
        keystore.selectBest()
        keystore.print_pop()
        if curgen % r_offspring_lim == r_offspring_lim - 1:  # random offspring generation
            print("random offspring generation")
            keystore.add_pop(initialize(pop_limit - top_select))
        else:
            orderings = set()
            for i in range(0, pop_limit - top_select):
                child = [0] * 26
                parent1 = keystore.keyspace[random.randint(0, top_select - 1)][0]
                parent2 = keystore.keyspace[random.randint(0, top_select - 1)][0]
                '''
                bias = random.randrange(1, biasing_value)
                for j in range(0, 26):
                    if j % bias != 0:
                        child[j] = parent1[j]
                    else:
                        child[j] = parent2[j]
                '''
                ranpos = random.randint(1, 25)
                child = list(parent1[:ranpos]+parent2[ranpos:])

                chance = random.randrange(0, 1)
                if chance < mut_prob:  # mutation on low probability
                    child[random.randint(0, 26 - 1)] = chr(random.randint(0, 25) + 65)  # change one random value
                                                                                        # by random amount
                orderings.add(tuple(child))
            keystore.add_pop(orderings)
        curgen = curgen + 1
        generations = generations + 1
        print("//////////////////////////////////////////////////////////////////////////////////////////////")


pop_limit = 250
generations = 10
top_select = 50
mut_prob = 0.2
r_offspring_lim = 30
biasing_value = 2
start_time = time.time()
keystore = Keystore()
keystore.add_pop(initialize(pop_limit))
keystore.print_pop()
genetic()