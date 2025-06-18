from utils.data import Data
from utils.logFiles import ExecutionLog
from utils.openFiles import get_file_path
from algorithm.genetic import GeneticOptimizer


param_grid = [
    dict(
        population_size=50,
        mutation_rate=0.25,
        crossover_size=10,
        replace_per_gen=12,
        max_steps=500,
    ),
    dict(
        population_size=100,
        mutation_rate=0.25,
        crossover_size=10,
        replace_per_gen=25,
        max_steps=500,
    ),
    dict(
        population_size=50,
        mutation_rate=0.25,
        crossover_size=10,
        replace_per_gen=12,
        max_steps=1000,
    ),
    dict(
        population_size=100,
        mutation_rate=0.25,
        crossover_size=10,
        replace_per_gen=25,
        max_steps=1000,
    ),
]

i = 1
while True:
    file_path = get_file_path(i)
    if file_path is None or "scenario2" in file_path:
        break
    try:
        data = Data(file_path)
        for params in param_grid:
            for iter in range(5):
                execution_log = ExecutionLog(file_path, iter, "Genetic", params)
                opt = GeneticOptimizer(data, **params)
                opt.run()

                best_ks = opt.best_knapsack
                best_profit = best_ks.get_profit()
                best_items = best_ks.get_items()

                execution_log.log_execution(best_profit, best_items)
    except Exception as e:
        print(e)
        print(f"Error in file {file_path}")
    i += 1
