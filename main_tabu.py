from algorithm.tabu import tabu_search
from utils.tools import Construcao 
from utils.data import Data
from utils.knapsack import Knapsack
import numpy as np
import os
from dotenv import load_dotenv
import time

load_dotenv(dotenv_path=".env") 
INSTANCES_PATH = os.getenv('INSTANCES')

data_1 = Data(f'{INSTANCES_PATH}/scenario1/correlated_sc1/1000/kpfs_2.txt')
m = Knapsack(data_1)
start_time = time.time()
c = Construcao(1)
initial_items = c.LCR(m)
m.replace_items(initial_items)
tabu_search(m, 5000, 100)
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
print(m.get_items())
print(m.get_profit())

