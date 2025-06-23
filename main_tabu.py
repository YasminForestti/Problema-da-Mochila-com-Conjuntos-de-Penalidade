from algorithm.tabu import tabu_search
from utils.tools import Construcao 
from utils.data import Data
from utils.knapsack import Knapsack
import numpy as np
from utils.logFiles import ExecutionLog
from utils.openFiles import get_file_path

numb_of_iter = [100, 500, 1000]
tabu_size = [10, 20, 30, 40, 50]
i = 1
while i < 31:
    file_path = get_file_path(i,mode='size')
    # if file_path is None or  'scenario2' in file_path:
    #     break
    try:
        data = Data(file_path)
        solution = Construcao(1)
        for max_iter in numb_of_iter:
            for size in tabu_size:
                for iter in range(5):
                    execution_log = ExecutionLog(file_path, iter, 'tabu', {'max_iter': max_iter, 'tabu_size': size})
                    mochila = Knapsack(data)
                    initial_items = solution.LCR(mochila)
                    mochila.replace_items(initial_items)
                    best_items, best_profit = tabu_search(mochila, max_iter, size)
                    execution_log.log_execution(best_profit, best_items)
    except: 
        print(f"Error in file {file_path}")
    print(f'{i}/30 done')
    i+=1

