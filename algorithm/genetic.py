from random import shuffle
from utils.knapsack import Knapsack
from utils.tools import Construcao
from utils.data import Data
from utils.knapsack import Knapsack
import numpy as np
from itertools import batched



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
    
    def __gt__(self, oth: GeneticIndivivdual) -> bool:
        self.knapsack.get_profit() > oth.knapsack.get_profit()

class GeneticOptimizer:

    def __init__(self, population_size: int, crossover_size: int, data: Data):
        self.crossover_size = crossover_size
        self.population_size = population_size
        GeneticOptimizer.gene_size = 30
        self.population = []

        starting_sacks = [Knapsack(data) for _ in range(self.population_size)]
        for ks in starting_sacks:
            c.LCR(ks)
            self.population += [GeneticIndivivdual(ks, 0.01)]

    def get_pairings(self) -> list[tuple[int, int]]:
        '''
        Create a list of indexes representing individuals in the population.
        '''
        idxs = list(range(self.population_size))
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

        gene_1 = first.knapsack.get_items()
        gene_2 = second.knapsack.get_items()

        start = np.random.randint(cls.gene_size)
        end = np.random.randint(start, cls.gene_size)
    
        tmp = gene_1[start:end].copy()
        gene_1[start:end] = gene_2[start:end]
        gene_2[start:end] = tmp
    
    def sort(self):
        self.population.sort()
        for i, d in enumerate(self.population, 1):
            print(f"{i}. {d.knapsack.get_profit()}")
if __name__ == "__main__":
    import os

    INSTANCES_PATH = os.getenv("INSTANCES")

    data_1 = Data(f"{INSTANCES_PATH}/scenario2/correlated_sc2/300/kpfs_1.txt")
    c = Construcao(1)

    opt = GeneticOptimizer(2, 30, data_1)
    # x = opt.cross(*opt.population)
    x = opt.population[0]
    print(x.knapsack.get_items())
    for _ in range(10):
        x.mutate()
    print(x.knapsack.get_items())
    # m.replace_items(initial_items)
    # tabu_search(m, 5000, 100)
    # end_time = time.time()
    # print(f"Time taken: {end_time - start_time} seconds")

