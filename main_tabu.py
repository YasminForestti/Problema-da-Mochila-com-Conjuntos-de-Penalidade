from algorithm.tabu import tabu_search
from utils.tools import Construcao
from utils.data import Data
from utils.knapsack import Knapsack
import numpy as np
from utils.logFiles import ExecutionLog
from utils.openFiles import get_file_path
from cProfile import Profile
from pstats import Stats, SortKey


numb_of_iter = [100, 500, 1000]
tabu_size = [10, 20, 30, 40, 50]
i = 1
file_path = get_file_path(i)

data = Data(file_path)
guloso = Construcao(1)

mochila = Knapsack(data)
initial_items = guloso.LCR(mochila)
mochila.replace_items(initial_items)

with Profile() as p:
    best_items, best_profit = tabu_search(mochila, 1000, 50)
s = Stats(p)
s.sort_stats(SortKey.TIME)
s.dump_stats("tabu.prof")
