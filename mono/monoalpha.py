import time
# from fitness import fit_word_check
from fitness import fit_freq_check
import random
import operator


class Keystore:

    def __init__(self):
        self.keyspace = []

    def add_pop(self, orderings):
        for key in orderings:
            count, res = fit_freq_check(key)
            self.keyspace.append((key, count, res))

    def print_pop(self):
        for x in self.keyspace:
            print(x)

    def sorter(self):
        self.keyspace.sort(key=operator.itemgetter(1), reverse=True)

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


def hillclimb():
    for tup in keystore.keyspace:
        flag = True
        comp_lim = tup[1]
        while flag:
            i = random.randrange(0, 26)
            tmp = list(tup[0])
            pos = random.randrange(0, 26)
            med = tmp[i]
            tmp[i] = tmp[pos]
            tmp[pos] = med
            wc, wl = fit_freq_check(tmp)
            if wc > comp_lim:
                flag = False
                keystore.keyspace.append((tuple(tmp), wc, wl))
                comp_lim = wc
                # aprint("climbed", end="")
                keystore.keyspace.remove(tup)


def genetic():
    global generations
    curgen = 0
    while generations > curgen:
        keystore.sorter()
        keystore.selectBest()
        keystore.print_pop()
        print("generation= ", curgen)
        if curgen % r_offspring_lim == r_offspring_lim - 1:  # random offspring generation
            print("random offspring generation")
            keystore.add_pop(initialize(pop_limit - top_select))
            hillclimb()
        else:
            orderings = set()
            for i in range(0, pop_limit - top_select):
                parent1 = keystore.keyspace[random.randint(0, top_select - 1)][0]
                parent2 = keystore.keyspace[random.randint(0, top_select - 1)][0]

                ranpos1 = random.randint(2, 10)
                ranpos2 = random.randint(18, 24)
                undone = []
                child = ['~']*26
                for j in range(0, ranpos1+1):
                    child[j] = parent1[j]
                for j in range(0, 26):
                    if not (chr(j+65) in child):
                        undone.append(chr(j+65))
                for j in range(ranpos2, 26):
                    if parent2[j] in undone:
                        child[j] = parent2[j]
                        undone.remove(parent2[j])
                z = 0
                random.shuffle(undone)
                for j in range(ranpos1, 26):
                    if child[j] == '~':
                        child[j] = undone[z]
                        z += 1
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


pop_limit = 100
generations = 10
top_select = 70
mut_prob = 0.2
r_offspring_lim = 30
biasing_value = 2
start_time = time.time()
keystore = Keystore()
keystore.add_pop(initialize(pop_limit))
keystore.print_pop()
genetic()

'''

	Approach 6:
	
		Hillclimbing applied.
		
		Fitness Function: Number of english words from a dictionary
		
		Crossover: Select two parents, two random positions from start and end, apply all starting genes to child. Apply ending genes that are not in starting, to end of child.
		Populate the middle with rest of the alphabet keeping consistency.
		
		parent1 = keystore.keyspace[random.randint(0, top_select - 1)][0]
                parent2 = keystore.keyspace[random.randint(0, top_select - 1)][0]

                ranpos1 = random.randint(2, 10)
                ranpos2 = random.randint(18, 24)
                undone = []
                child = ['~']*26
                for j in range(0, ranpos1+1):
                    child[j] = parent1[j]
                for j in range(0, 26):
                    if not (chr(j+65) in child):
                        undone.append(chr(j+65))
                for j in range(ranpos2, 26):
                    if parent2[j] in undone:
                        child[j] = parent2[j]
                        undone.remove(parent2[j])
                z = 0
                random.shuffle(undone)
                for j in range(ranpos1, 26):
                    if child[j] == '~':
                        child[j] = undone[z]
                        z += 1
             	
		Problem: Stuck in local optima. But keys are consistent till the end. No more fatal issues.
		
	
		
	Approach 7: 


		Hillclimbing applied.
		
		Fitness Function: Frequency distribution of letters in english against cracked sample.
		
		Crossover: Same as approach 6
		
		Problem: Convergence is slow. Stuck in local optima.



'''