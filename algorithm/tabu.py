import utils.tools as tools
from utils.knapsack import Knapsack
import numpy as np

def  tabu_search(knapsack: Knapsack, max_iter: int, max_tabu_size: int):
    tabu_list = [knapsack.get_items()]
    iter = 0 
    best_knapsack = knapsack.clone()
    while iter < max_iter:
        items = best_knapsack.get_items()
        best_solution = best_knapsack.get_profit()
        neighbors = _generate_neighbors(items)

        for neighbor in neighbors:
            current_knapsack = best_knapsack.clone()
            current_knapsack.replace_items(neighbor)
            if neighbor not in tabu_list:
                continue
            if current_knapsack.is_valid():
                if current_knapsack.get_profit() > best_solution:
                    best_knapsack = current_knapsack
                    tabu_list.append(neighbor)
        iter += 1
    return best_knapsack

def _generate_neighbors(items: np.ndarray):
    neighbors = []
    for i in range(len(items)):
        neighbor = items.copy()
        neighbor[i] = 1 if neighbor[i] == 0 else 0
        neighbors.append(neighbor)
