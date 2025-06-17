from random import shuffle
from utils.knapsack import Knapsack
import numpy as np
from itertools import batched
from utils.data import Data
from copy import deepcopy



from utils.tools import Construcao
c = Construcao(1)


class GeneticIndivivdual:

    def __init__(self, starting_knapsack: Knapsack, mutation_rate: float):
        self.knapsack = starting_knapsack
        self.gene_size = len(self.knapsack.get_items())
        self.mutation_rate = mutation_rate

    def mutate(self):
        '''
        Decide whether mutation should occur and perform the mutation in
        case it decides to do so.
        '''
        if np.random.uniform(0, 1) < self.mutation_rate:
            self._mutate_gene()

    def _mutate_gene(self):
        '''
        Change a single item in the knapsack, inverting its value.
        '''
        idx = np.random.randint(self.gene_size - 1)
        # This violaters Knapsack's instance isolation for perfomance's sake
        self.knapsack._items[idx] = int(not self.knapsack._items[idx])
    
    def __gt__(self, oth) -> bool:
        return self.knapsack.get_profit() > oth.knapsack.get_profit()

class GeneticOptimizer:

    def __init__(self, data: Data, 
                 population_size: int, mutation_rate: float,
                 crossover_size: int, replace_per_gen: int, 
                 max_steps: int):
        self.crossover_size = crossover_size
        self.population_size = population_size
        GeneticOptimizer.gene_size = 30
        self.population: list[GeneticIndivivdual] = []
        self.killAmt = replace_per_gen
        self.max_steps = max_steps
        

        starting_sacks = [Knapsack(data) for _ in range(self.population_size)]
        for ks in starting_sacks:
            c.LCR(ks)
            self.population += [GeneticIndivivdual(ks, mutation_rate)]

    def step(self):
        
        for e in self.population:
            e.mutate()

        # self.population.sort(reverse=False)
        self.population.sort()
        self.population = self.population[:-self.killAmt]

        newborns = []
        for i, j in self.get_pairings():
            new_1, new_2 = self.cross(self.population[i], self.population[j])
            newborns += [new_1, new_2]
            if len(newborns) >= self.killAmt: break

        self.population += newborns[:self.killAmt]

    def run(self):
        for gen in range(1, self.max_steps + 1):
            self.step()
            print(f"[Gen {gen}] Best score: {self.population[0].knapsack.get_profit()}")


    def get_pairings(self) -> list[tuple[int, int]]:
        '''
        Create a list of indexes representing individuals in the population.
        '''
        idxs = list(range(len(self.population)))
        shuffle(idxs)
        return list(batched(idxs, 2))

    @classmethod
    def cross(cls, first: GeneticIndivivdual, second: GeneticIndivivdual):
        '''
        Mix the genes of the first and second individual.
        The size of the change is determined by a crossover_size, and
        the switched parts happen in the same part of each gene, in a
        continuous manner.
        '''
        
        first = deepcopy(first)
        second = deepcopy(second)

        gene_1 = first.knapsack.get_items()
        gene_2 = second.knapsack.get_items()

        start = np.random.randint(cls.gene_size)
        end = np.random.randint(start, cls.gene_size)
    
        tmp = gene_1[start:end].copy()

        
        gene_1[start:end] = gene_2[start:end]
        gene_2[start:end] = tmp

        return first, second
    
    def viz_sort(self):
        self.population.sort(reverse=True)
        for i, d in enumerate(self.population, 1):
            print(f"{i}: $ {d.knapsack.get_profit()}")

