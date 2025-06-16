from utils.knapsack import Knapsack
from utils.tools import Construcao
from utils.data import Data
from utils.knapsack import Knapsack
import numpy as np
from itertools import batched


class GeneticOptimizer:

    def __init__(self, population_size: int, crossover_size: int):
        self.crossover_size = crossover_size
        self.population_size = population_size
        self.gene_size = 30

    def get_pairings(self):
        idxs = list(range(self.population_size))
        shuffle(idxs)
        batched(idxs, 2)

    @staticmethod
    def cross(first: GeneticOptimizer, second: GeneticOptimizer):
        start = np.random.randint(self.gene_size)
        tmp = first.knapsack.get_items().copy()


class GeneticIndivivdual:

    def __init__(self, initial_data: Knapsack, mutation_rate: float):
        self.knapsack = initial_data
        self.gene_size = len(initial_data.get_items())

    def mutate(self):
        idx = np.random.randint(self.gene_size - 1)
        # This violaters Knapsack's instance isolation for perfomance's sake
        self.knapsack._items[idx] = int(not self.knapsack._items[idx])


INSTANCES_PATH = os.getenv("INSTANCES")

data_1 = Data(f"{INSTANCES_PATH}/scenario2/correlated_sc2/300/kpfs_1.txt")
m = Knapsack(data_1)
x = np.zeros(300)
x[2] = 1
print(m.replace_items(x))

# start_time = time.time()x``
# c = Construcao(1)
# initial_Items = c.LCR(m)
# m.replace_items(initial_items)
# tabu_search(m, 5000, 100)
# end_time = time.time()
# print(f"Time taken: {end_time - start_time} seconds")
print(m.get_items().shape)
print(m.get_profit())
print(m.is_valid())
