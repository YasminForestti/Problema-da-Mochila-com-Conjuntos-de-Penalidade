from random import shuffle
from utils.knapsack import Knapsack
from utils.tools import Construcao
from utils.data import Data
from utils.knapsack import Knapsack
import numpy as np
from itertools import batched



class GeneticIndivivdual:

    def __init__(self, initial_data: Data, mutation_rate: float):
        self.knapsack = Knapsack(initial_data)
        self.gene_size = len(self.knapsack.get_items())

    def mutate(self):
        idx = np.random.randint(self.gene_size - 1)
        # This violaters Knapsack's instance isolation for perfomance's sake
        self.knapsack._items[idx] = int(not self.knapsack._items[idx])


class GeneticOptimizer:

    def __init__(self, population_size: int, crossover_size: int, data: Data):
        self.crossover_size = crossover_size
        self.population_size = population_size
        GeneticOptimizer.gene_size = 30
        self.population = [GeneticIndivivdual(data, 0.01) for _ in range(self.population_size)]

    def get_pairings(self) -> list[tuple[int, int]]:
        idxs = list(range(self.population_size))
        shuffle(idxs)
        return list(batched(idxs, 2))

    @classmethod
    def cross(cls, first: GeneticIndivivdual, second: GeneticIndivivdual):
        print(first.knapsack.get_items())
        print(second.knapsack.get_items())

        start = np.random.randint(cls.gene_size)
        end = np.random.randint(start, cls.gene_size)
        print(start, end)
        tmp = first.knapsack.get_items().copy()

if __name__ == "__main__":
    import os

    INSTANCES_PATH = os.getenv("INSTANCES")

    data_1 = Data(f"{INSTANCES_PATH}/scenario2/correlated_sc2/300/kpfs_1.txt")
    opt = GeneticOptimizer(2, 30, data_1)
    x = opt.cross(*opt.population)
    print(x)
    # start_time = time.time()x``
    # c = Construcao(1)
    # initial_Items = c.LCR(m)
    # m.replace_items(initial_items)
    # tabu_search(m, 5000, 100)
    # end_time = time.time()
    # print(f"Time taken: {end_time - start_time} seconds")

