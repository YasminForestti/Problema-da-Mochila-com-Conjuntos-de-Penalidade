from random import shuffle
from utils.knapsack import Knapsack
import numpy as np
from itertools import batched
from utils.data import Data
from copy import deepcopy


from utils.tools import Construcao

c = Construcao(1)


class GeneticIndivivdual:

    def __init__(
        self, starting_items: np.array, knapsack: Knapsack, mutation_rate: float
    ):
        self.items = starting_items
        self.gene_size = len(self.items)
        self.mutation_rate = mutation_rate
        self.knapsack = knapsack

    def mutate(self):
        """
        Decide whether mutation should occur and perform the mutation in
        case it decides to do so.
        """
        if np.random.uniform(0, 1) < self.mutation_rate:
            self._mutate_gene()

    def _mutate_gene(self):
        """
        Change a single item in the knapsack, inverting its value.
        """
        idx = np.random.randint(self.gene_size - 1)
        self.items[idx] = int(not self.items[idx])

    @property
    def value(self) -> float:
        return self.knapsack.get_profit_given_items(self.items)

    def __gt__(self, oth) -> bool:
        return self.value > oth.value


class GeneticOptimizer:

    def __init__(
        self,
        data: Data,
        population_size: int,
        mutation_rate: float,
        crossover_size: int,
        replace_per_gen: int,
        max_steps: int,
    ):
        self.crossover_size = crossover_size
        self.population_size = population_size
        self.gene_size = 30
        self.population: list[GeneticIndivivdual] = []
        self.killAmt = replace_per_gen
        self.max_steps = max_steps
        self.best = None
        self.best_val = -999999
        self.mutation_rate = mutation_rate

        self.knapsack = Knapsack(data)
        for i in range(population_size):
            c.LCR(self.knapsack)
            items = self.knapsack.get_items().copy()
            self.knapsack.replace_items(np.zeros_like(items))
            self.population += [GeneticIndivivdual(items, self.knapsack, mutation_rate)]

    def step(self):

        for e in self.population:
            e.mutate()

        self.population.sort(reverse=True)
        # self.viz()
        self.population = self.population[: -self.killAmt]
        newborns = []
        for i, j in self.get_pairings():
            new_1, new_2 = self.cross(self.population[i], self.population[j])
            newborns += [new_1, new_2]
            if len(newborns) >= self.killAmt:
                break

        self.population += newborns[: self.killAmt]

    def run(self):
        for gen in range(1, self.max_steps + 1):
            self.step()

            gen_best = self.population[0]
            if gen_best.value > self.best_val:
                self.best = deepcopy(gen_best)
                self.best_val = gen_best.value

            print(
                f"[Gen {gen}] Best generational score: {self.population[0].value} | Best overall: {self.best_val}"
            )
        return self.best_knapsack

    def get_pairings(self) -> list[tuple[int, int]]:
        """
        Create a list of indexes representing individuals in the population.
        """
        size = len(self.population) >> 1 << 1
        idxs = list(range(size))
        shuffle(idxs)
        return list(batched(idxs, 2))

    def cross(self, first: GeneticIndivivdual, second: GeneticIndivivdual):
        """
        Mix the genes of the first and second individual.
        The size of the change is determined by a crossover_size, and
        the switched parts happen in the same part of each gene, in a
        continuous manner.
        """

        gene_1 = first.items.copy()
        gene_2 = second.items.copy()

        start = np.random.randint(self.gene_size)
        end = np.random.randint(start, self.gene_size)

        tmp = gene_1[start:end].copy()

        gene_1[start:end] = gene_2[start:end]
        gene_2[start:end] = tmp

        first = GeneticIndivivdual(gene_1, self.knapsack, self.mutation_rate)
        second = GeneticIndivivdual(gene_2, self.knapsack, self.mutation_rate)

        return first, second

    @property
    def best_knapsack(self) -> Knapsack:
        self.knapsack.replace_items(self.best.items)
        return self.knapsack

    def viz(self):
        for i, d in enumerate(self.population, 1):
            print(f"{i}: $ {d.knapsack.get_profit()}")
        input()
