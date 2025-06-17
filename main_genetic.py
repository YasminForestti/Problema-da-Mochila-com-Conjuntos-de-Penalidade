from algorithm.genetic import GeneticOptimizer
from utils.data import Data


if __name__ == "__main__":
    import os

    INSTANCES_PATH = os.getenv("INSTANCES")

    data_1 = Data(f"{INSTANCES_PATH}/scenario2/correlated_sc2/300/kpfs_1.txt")

    opt = GeneticOptimizer(data_1, 
                           population_size=100,
                           mutation_rate=0.25,
                           crossover_size=10,
                           replace_per_gen=25,
                           max_steps=1000
                           )

    opt.run()

