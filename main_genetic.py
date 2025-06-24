from utils.data import Data
from utils.logFiles import ExecutionLog
from utils.openFiles import get_file_path
from algorithm.genetic import GeneticOptimizer
from algorithm.genetic_constraintless import GeneticOptimizerNoConstraint
from multiprocessing import Pool

USE_PENALIZED = True
if USE_PENALIZED:
    print("Starting without constraints")

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


def test_alg(iter: int):

    execution_log = ExecutionLog(file_path, iter, "Genetic", params)
    if USE_PENALIZED:
        opt = GeneticOptimizerNoConstraint(data, **params)
    else:
        opt = GeneticOptimizer(data, **params)
    best_ks = opt.run()
    best_profit = best_ks.get_profit()
    best_items = best_ks.get_items()

    execution_log.log_execution(best_profit, best_items)


i = 1

while i < 31:
    file_path = get_file_path(i)
    if file_path is None or "scenario2" in file_path:
        break
    try:
        data = Data(file_path)
        for params in param_grid:
            with Pool(5) as p:
                _ = p.map(test_alg, list(range(5)))

    except Exception as e:
        print(e)
        print(f"Error in file {file_path}")
    i += 1
