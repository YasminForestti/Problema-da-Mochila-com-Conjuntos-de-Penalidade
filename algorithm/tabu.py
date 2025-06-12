import utils.tools as tools
from utils.knapsack import Knapsack
import numpy as np

def  tabu_search(knapsack: Knapsack, max_iter: int, max_tabu_size: int):
    best_items = knapsack.get_items()
    best_profit = knapsack.get_profit()
    iter = 0 
    tabu_list = [best_items[:]]
    while iter < max_iter:
        neighbors = _generate_neighbors(best_items)
        for neighbor in neighbors:
            knapsack.replace_items(neighbor)
            if knapsack.is_valid():
                if not any(np.array_equal(neighbor, lst) for lst in tabu_list):
                    if knapsack.get_profit() > best_profit:
                        best_items = knapsack.get_items()
                        best_profit = knapsack.get_profit()
                        tabu_list.append(neighbor)
                        if len(tabu_list) > max_tabu_size:
                            tabu_list.pop(0)
        iter += 1
    return best_items, best_profit

def _generate_neighbors(items: np.ndarray):
    neighbors = []
    for i in range(len(items)):
        neighbor = items.copy()
        neighbor[i] = 1 if neighbor[i] == 0 else 0
        neighbors.append(neighbor)
    return neighbors
