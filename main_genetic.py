from algorithm.genetic import GeneticOptimizer
from utils.data import Data


if __name__ == "__main__":
    import os

    INSTANCES_PATH = os.getenv("INSTANCES")

    data_1 = Data(f"{INSTANCES_PATH}/scenario2/correlated_sc2/300/kpfs_1.txt")

    opt = GeneticOptimizer(data_1, 50, 30, 0.1, 5, 200)
    # x = opt.cross(*opt.population)
    # x = opt.population[0]
    # print(x.knapsack.get_items())
    # for _ in range(10):
    opt.run()
        # x.mutate()
    # print(x.knapsack.get_items())
    # m.replace_items(initial_items)
    # tabu_search(m, 5000, 100)
    # end_time = time.time()
    # print(f"Time taken: {end_time - start_time} seconds")

